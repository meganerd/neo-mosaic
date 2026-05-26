# neo-mosaic

> NCSA Mosaic-inspired retro browser theme for Firefox and Chrome/Chromium.

Brings back the look and feel of the original NCSA Mosaic web browser — the first graphical browser that brought the web to the masses in 1993. Features the classic Mosaic logo and the original grey/blue color palette.

![NCSA Mosaic Logo](shared/mosaic-logo.png)

## Structure

```
mosaic-browser-theme/
├── firefox/       # Firefox static theme
├── chrome/        # Chrome/Chromium theme
├── shared/        # Shared assets (logo, reference images)
└── README.md
```

## Firefox

1. Open `about:addons`
2. Click the gear icon → "Install Add-on From File..."
3. Select `firefox/mosaic-theme.zip`
4. Or: open `about:debugging#/runtime/this-firefox` → "Load Temporary Add-on" → select any file in `firefox/`

## Chrome / Chromium

1. Open `chrome://extensions/`
2. Enable "Developer mode"
3. Click "Load unpacked"
4. Select the `chrome/` directory

## License

MIT
