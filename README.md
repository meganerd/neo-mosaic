# neo-mosaic

> NCSA Mosaic-inspired retro browser theme for Firefox and Chrome/Chromium.

Brings back the look and feel of the original NCSA Mosaic web browser — the first graphical browser that brought the web to the masses in 1993. Classic Motif/Windows 3.1 grey chrome with navy link accents.

## Variants

Two logo variants available:

| Variant | Logo | Firefox | Chrome | 
|---------|------|---------|--------|
| **diamond** | Geometric diamond tiles (original NCSA Mosaic logo by Colleen Bushell) | `firefox/diamond/` | `chrome/diamond/` |
| **globe** | Spinning planet Earth throbber (introduced in Mosaic 2.0, November 1993) | `firefox/globe/` | `chrome/globe/` |

![Diamond logo](shared/mosaic-logo.png) ![Globe logo](shared/spinning-globe.png)

## Structure

```
neo-mosaic/
├── firefox/
│   ├── diamond/         # Firefox — diamond variant
│   │   ├── manifest.json
│   │   ├── mosaic-header.png
│   │   └── icon-*.png
│   └── globe/           # Firefox — globe variant
│       ├── manifest.json
│       ├── mosaic-header.png
│       └── icon-*.png
├── chrome/
│   ├── diamond/         # Chrome — diamond variant
│   │   ├── manifest.json
│   │   ├── mosaic-header.png
│   │   └── icon-*.png
│   └── globe/           # Chrome — globe variant
│       ├── manifest.json
│       ├── mosaic-header.png
│       └── icon-*.png
├── shared/              # SVG/PNG source assets
└── README.md
```

## Installing

### Firefox
1. Open `about:addons`
2. Click the gear icon → **Install Add-on From File...**
3. Select the `.xpi` from a release, or:
   - Open `about:debugging#/runtime/this-firefox`
   - Click **Load Temporary Add-on...**
   - Select `firefox/diamond/manifest.json` or `firefox/globe/manifest.json`

### Chrome / Chromium
1. Open `chrome://extensions/`
2. Enable **Developer mode**
3. Click **Load unpacked**
4. Select `chrome/diamond/` or `chrome/globe/`

## Color Palette

| Shade | Color | Role |
|-------|-------|------|
| `#C0C0C0` | Motif grey | Window frame, toolbars, sidebars |
| `#D4D4D4` | Light grey | Selected tabs, hover states |
| `#A8A8A8` | Dark grey | Inactive frames |
| `#808080` | Shadow grey | Borders, separators |
| `#FFFFFF` | White | URL/omnibox fields |
| `#000000` | Black | Text |
| `#000080` | Navy | Links, bookmarks, highlights |

## License

MIT
