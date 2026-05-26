# neo-mosaic

> NCSA Mosaic-inspired retro browser theme for Firefox and Chrome/Chromium.

Brings back the look and feel of the original NCSA Mosaic web browser — the first graphical browser that brought the web to the masses in 1993. Features the classic geometric diamond logo in rust, teal, yellow-green, and gold, set against the original Motif/Windows 3.1 grey chrome.

![NCSA Mosaic Logo](shared/mosaic-logo.png)

## Structure

```
neo-mosaic/
├── firefox/       # Firefox static theme (manifest v2)
│   ├── manifest.json
│   ├── mosaic-header.png
│   ├── icon-*.png
│   └── README.md
├── chrome/        # Chrome/Chromium theme (manifest v3)
│   ├── manifest.json
│   ├── mosaic-header.png
│   ├── icon-*.png
│   └── README.md
├── shared/        # Shared SVG/PNG assets
└── README.md
```

## Themes

| Browser | Type | Install |
|---------|------|---------|
| Firefox | Static theme | `about:addons` → Install from file → `firefox/manifest.json` |
| Chrome | Manifest V3 theme | `chrome://extensions/` → Load unpacked → `chrome/` |

## Color Palette

The theme recreates the classic 1993 browser chrome:

| Shade | Color | Role |
|-------|-------|------|
| `#C0C0C0` | Motif grey | Window frame, toolbars, sidebars |
| `#D4D4D4` | Light grey | Selected tabs, hover states |
| `#A8A8A8` | Dark grey | Inactive frames |
| `#808080` | Shadow grey | Borders, separators |
| `#FFFFFF` | White | URL/omnibox fields |
| `#000000` | Black | Text |
| `#000080` | Navy | Links, bookmarks, highlights |
| `#B84B16` | Rust | Logo diamond |
| `#005953` | Dark teal | Logo diamond |
| `#B2BB1E` | Yellow-green | Logo diamond |
| `#C5A901` | Gold | Logo diamond |

## License

MIT
