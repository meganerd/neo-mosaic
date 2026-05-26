# neo-mosaic — Chrome / Chromium

## Install

1. Open `chrome://extensions/`
2. Enable **Developer mode** (top right toggle)
3. Click **Load unpacked**
4. Select the `chrome/` directory

## Packaging

```bash
cd chrome/diamond/
zip -r ../mosaic-chrome-theme.zip manifest.json mosaic-header.png icon-*.png
```

Then drag the `.zip` onto `chrome://extensions/` or publish to the Chrome Web Store.

## Colors

| Element | Color | Description |
|---------|-------|-------------|
| Frame / Toolbar | `rgb(192,192,192)` | Classic Motif grey |
| Tab / Toolbar text | `rgb(0,0,0)` | Black |
| Bookmark / Link text | `rgb(0,0,128)` | Navy blue |
| Omnibox background | `rgb(255,255,255)` | White field |
| NTP Link | `rgb(0,0,128)` | Navy underline links |

## License

MIT
