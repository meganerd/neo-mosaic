#!/usr/bin/env python3
"""Generate marble header + wallpaper assets for neo-mosaic browser theme.

90s Motif style: raised/beveled 3D borders, blocky corners, cool marble texture.
Diamond and globe variants get distinct header designs.
"""

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import cairosvg
import io
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHARED = os.path.join(BASE_DIR, "shared")


# 90s Cool Blue Marble Palettes
LIGHT_COLORS = {
    "base": (240, 242, 248),
    "vein1": (208, 216, 228),
    "vein2": (188, 198, 214),
    "accent": (216, 208, 224),
}

DARK_COLORS = {
    "base": (40, 44, 52),
    "vein1": (72, 80, 92),
    "vein2": (88, 100, 116),
    "accent": (60, 52, 72),
}


# Motif 90s Bevel Color Schemes
MARBLE_MOTIF_LIGHT = {
    "highlight": (255, 255, 255),
    "light": (232, 234, 240),
    "base": (224, 226, 234),
    "dark": (168, 172, 180),
    "shadow": (100, 104, 112),
    "marble": LIGHT_COLORS,
}

MARBLE_MOTIF_DARK = {
    "highlight": (80, 84, 92),
    "light": (56, 60, 68),
    "base": (40, 44, 52),
    "dark": (28, 30, 36),
    "shadow": (16, 18, 22),
    "marble": DARK_COLORS,
}


# Noise Generation

def fbm_noise(width, height, scale=0.03, octaves=6, seed=None):
    if seed is not None:
        np.random.seed(seed)
    rows = np.arange(height)
    cols = np.arange(width)
    y, x = np.meshgrid(rows, cols, indexing='ij')
    noise = np.zeros((height, width))
    amplitude = 1.0
    frequency = 1.0
    max_value = 0.0
    for _ in range(octaves):
        phase = np.random.uniform(0, 2 * np.pi)
        noise += amplitude * (
            np.sin(x * frequency * scale + phase) *
            np.cos(y * frequency * scale * 0.7 + phase * 1.3)
        )
        max_value += amplitude
        amplitude *= 0.5
        frequency *= 2.0
    return noise / max_value


def marble_texture(width, height, colors, scale=0.02, seed=42):
    n1 = fbm_noise(width, height, scale=scale, octaves=6, seed=seed)
    n2 = fbm_noise(width, height, scale=scale * 2.5, octaves=4, seed=seed + 1)
    n3 = fbm_noise(width, height, scale=scale * 0.4, octaves=3, seed=seed + 2)
    veins = np.sin(n1 * 6.0 + np.sin(n2 * 8.0) * 1.5) * 0.5 + 0.5
    swirl = n3 * 0.5 + 0.5
    result = np.zeros((height, width, 3), dtype=np.uint8)
    b = np.array(colors["base"], dtype=np.float32)
    v1 = np.array(colors["vein1"], dtype=np.float32)
    v2 = np.array(colors["vein2"], dtype=np.float32)
    ac = np.array(colors["accent"], dtype=np.float32)
    for c in range(3):
        base_mod = b[c] + (swirl - 0.5) * 8.0
        vein_color = v1[c] + (v2[c] - v1[c]) * (n2 * 0.5 + 0.5)
        accent_mask = (np.sin(n1 * 12.0 + n3 * 5.0) * 0.5 + 0.5) > 0.85
        vein_color = np.where(accent_mask, ac[c], vein_color)
        result[:, :, c] = np.clip(
            base_mod * (1 - veins * 0.35) + vein_color * (veins * 0.35),
            0, 255
        ).astype(np.uint8)
    return result


# Motif Bevel Drawing

def draw_beveled_frame(draw, x, y, w, h, motif, raised=True, width=2):
    top_left = motif["highlight"] if raised else motif["shadow"]
    bottom_right = motif["shadow"] if raised else motif["highlight"]
    for i in range(width):
        draw.line([(x + i, y + i), (x + w - 1 - i, y + i)], fill=top_left)
        draw.line([(x + i, y + i), (x + i, y + h - 1 - i)], fill=top_left)
        draw.line([(x + i, y + h - 1 - i), (x + w - 1 - i, y + h - 1 - i)], fill=bottom_right)
        draw.line([(x + w - 1 - i, y + i), (x + w - 1 - i, y + h - 1 - i)], fill=bottom_right)


def draw_beveled_rect(draw, x, y, w, h, motif, raised=True, fill=None):
    if fill:
        ix, iy, iw, ih = x + 2, y + 2, w - 4, h - 4
        if iw > 0 and ih > 0:
            draw.rectangle([ix, iy, ix + iw - 1, iy + ih - 1], fill=fill)
    draw_beveled_frame(draw, x, y, w, h, motif, raised=raised)


# Header Generation

def render_svg(svg_path, width, height):
    png_data = cairosvg.svg2png(url=svg_path, output_width=width, output_height=height)
    return Image.open(io.BytesIO(png_data)).convert('RGBA')


def generate_header_diamond(motif, output_path, width=3000, height=200):
    print(f"  diamond header: {output_path}")
    colors = motif["marble"]
    tex = marble_texture(width, height, colors, scale=0.015, seed=42)
    img = Image.fromarray(tex, 'RGB')
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    draw = ImageDraw.Draw(img)

    # Chiseled frame
    draw.line([(0, 0), (width, 0)], fill=motif["highlight"])
    draw.line([(0, 1), (width, 1)], fill=motif["light"])
    draw.line([(0, height - 2), (width, height - 2)], fill=motif["shadow"])
    draw.line([(0, height - 1), (width, height - 1)], fill=motif["dark"])

    # Raised panel behind logo area
    draw_beveled_rect(draw, 20, 20, 540, 160, motif, raised=True, fill=motif["base"])

    # Composite SVG overlay
    svg_path = os.path.join(SHARED, "mosaic-header.svg")
    overlay = render_svg(svg_path, width, height)
    img = Image.alpha_composite(img.convert('RGBA'), overlay)

    # Sunken URL bar
    draw_beveled_rect(draw, 580, 100, 580, 26, motif, raised=False, fill=(255, 255, 255))

    # Bottom bevel separator
    draw.line([(0, height - 4), (width, height - 4)], fill=motif["highlight"])
    draw.line([(0, height - 3), (width, height - 3)], fill=motif["light"])
    draw.line([(0, height - 1), (width, height - 1)], fill=motif["dark"])

    img.convert('RGB').save(output_path, 'PNG')


def generate_header_globe(motif, output_path, width=3000, height=200):
    print(f"  globe header: {output_path}")
    colors = motif["marble"]
    tex = marble_texture(width, height, colors, scale=0.015, seed=55)
    img = Image.fromarray(tex, 'RGB')
    img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
    draw = ImageDraw.Draw(img)

    # Chiseled frame
    draw.line([(0, 0), (width, 0)], fill=motif["highlight"])
    draw.line([(0, 1), (width, 1)], fill=motif["light"])
    draw.line([(0, height - 2), (width, height - 2)], fill=motif["shadow"])
    draw.line([(0, height - 1), (width, height - 1)], fill=motif["dark"])

    # Composite globe SVG overlay
    svg_path = os.path.join(SHARED, "globe-header.svg")
    overlay = render_svg(svg_path, width, height)
    img = Image.alpha_composite(img.convert('RGBA'), overlay)

    # Sunken URL bar
    draw_beveled_rect(draw, 560, 100, 580, 26, motif, raised=False, fill=(255, 255, 255))

    # Bottom bevel
    draw.line([(0, height - 4), (width, height - 4)], fill=motif["highlight"])
    draw.line([(0, height - 3), (width, height - 3)], fill=motif["light"])
    draw.line([(0, height - 1), (width, height - 1)], fill=motif["dark"])

    img.convert('RGB').save(output_path, 'PNG')


def generate_icon(colors, logo_svg_path, output_path, size=128):
    print(f"  icon {size}: {output_path}")
    tex = marble_texture(size, size, colors, scale=0.04, seed=42)
    img = Image.fromarray(tex, 'RGB')
    overlay = render_svg(logo_svg_path, size, size)
    result = Image.new('RGBA', (size, size))
    result.paste(img, (0, 0))
    result = Image.alpha_composite(result, overlay)
    result.convert('RGB').save(output_path, 'PNG')


def generate_marble_icons(colors, output_dir, logo_svg_path, sizes):
    os.makedirs(output_dir, exist_ok=True)
    for size in sizes:
        path = os.path.join(output_dir, f"icon-{size}.png")
        generate_icon(colors, logo_svg_path, path, size=size)


def generate_wallpaper(motif, output_path, svg_overlays=None, width=1920, height=1080):
    print(f"  wallpaper: {output_path}")
    colors = motif["marble"]
    tex = marble_texture(width, height, colors, scale=0.008, seed=42)
    img = Image.fromarray(tex, 'RGB')
    img = img.convert('RGBA')
    draw = ImageDraw.Draw(img)

    # Outer beveled frame
    bw = 8
    for i in range(bw):
        draw.rectangle([i, i, width - 1 - i, height - 1 - i],
                       outline=motif["shadow"] if i == 0 else None)
    draw_beveled_frame(draw, bw, bw, width - bw * 2, height - bw * 2,
                       motif, raised=True, width=3)

    if svg_overlays:
        for svg_path, (pos_x, pos_y, logo_size) in svg_overlays:
            overlay = render_svg(svg_path, logo_size, logo_size)
            img.paste(overlay, (pos_x, pos_y), overlay)

    img.convert('RGB').save(output_path, 'PNG')


def main():
    print("=" * 60)
    print("neo-mosaic Marble Asset Generator")
    print("Style: 90s Cool Blue Marble + Motif Beveled UI")
    print("=" * 60)

    diamond_svg = os.path.join(SHARED, "mosaic-logo.svg")
    globe_svg = os.path.join(SHARED, "spinning-globe.svg")

    # Firefox
    print("\n[Firefox marble]")
    ff_dir = os.path.join(BASE_DIR, "firefox", "marble")
    os.makedirs(ff_dir, exist_ok=True)
    generate_header_diamond(MARBLE_MOTIF_LIGHT, os.path.join(ff_dir, "marble-header.png"))
    generate_marble_icons(LIGHT_COLORS, ff_dir, diamond_svg, [16, 32, 48, 96, 128])

    # Chrome
    print("\n[Chrome marble]")
    ch_dir = os.path.join(BASE_DIR, "chrome", "marble")
    os.makedirs(ch_dir, exist_ok=True)
    generate_header_diamond(MARBLE_MOTIF_LIGHT, os.path.join(ch_dir, "marble-header.png"))
    generate_marble_icons(LIGHT_COLORS, ch_dir, diamond_svg, [16, 32, 48, 128])

    # Opera GX
    print("\n[Opera GX marble]")
    op_dir = os.path.join(BASE_DIR, "opera", "marble")
    os.makedirs(op_dir, exist_ok=True)
    wp_dir = os.path.join(op_dir, "wallpaper")
    os.makedirs(wp_dir, exist_ok=True)

    generate_icon(LIGHT_COLORS, diamond_svg, os.path.join(op_dir, "icon_512.png"), size=512)

    both_logos = [
        (os.path.join(SHARED, "spinning-globe.svg"), (100, 100, 512)),
        (os.path.join(SHARED, "mosaic-logo.svg"), (1308, 100, 512)),
    ]

    generate_wallpaper(MARBLE_MOTIF_LIGHT, os.path.join(wp_dir, "light.png"), svg_overlays=both_logos)
    generate_wallpaper(MARBLE_MOTIF_DARK, os.path.join(wp_dir, "dark.png"), svg_overlays=both_logos)

    print("\n" + "=" * 60)
    print("All done! Assets use:")
    print("  • Cool blue-grey marble (not brown)")
    print("  • Motif-style beveled/raised 3D borders")
    print("  • Opera wallpaper has diamond + globe logos embedded")
    print("  =")

if __name__ == "__main__":
    main()
