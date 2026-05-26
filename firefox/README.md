# neo-mosaic — Firefox

## Install (Firefox Add-ons)

Packaged as a static theme. To install:

**From a file:**
1. Open `about:addons`
2. Click the gear icon → **Install Add-on From File...**
3. Select `mosaic-theme.zip` (package the `firefox/` directory)

**Temporary install (development):**
1. Open `about:debugging#/runtime/this-firefox`
2. Click **Load Temporary Add-on...**
3. Select `firefox/manifest.json`

## Building

```bash
cd firefox/
zip -r ../mosaic-theme.xpi manifest.json mosaic-header.png icon-*.png
```

## Colors

| Element | Color | Description |
|---------|-------|-------------|
| Frame / Toolbar | `#C0C0C0` | Classic Motif grey |
| Tab text | `#000000` | Black |
| Bookmark / Link text | `#000080` | Navy blue |
| URL bar | `#FFFFFF` | White field |
| Borders | `#808080` | Dark grey bevel |
| Highlight | `#000080` | Navy selection |
| New Tab Page | `#C0C0C0` | Grey background |

## License

MIT
