VERSION ?= $(shell python3 -c "import json; print(json.load(open('firefox/diamond/manifest.json'))['version'])")

XPI_DIAMOND   := neo-mosaic-firefox-diamond-$(VERSION).xpi
XPI_GLOBE     := neo-mosaic-firefox-globe-$(VERSION).xpi
XPI_MARBLE    := neo-mosaic-firefox-marble-$(VERSION).xpi
ZIP_DIAMOND   := neo-mosaic-chrome-diamond-$(VERSION).zip
ZIP_GLOBE     := neo-mosaic-chrome-globe-$(VERSION).zip
ZIP_MARBLE    := neo-mosaic-chrome-marble-$(VERSION).zip
OPERA_ZIP_DIAMOND := neo-mosaic-opera-diamond-$(VERSION).zip
OPERA_ZIP_GLOBE   := neo-mosaic-opera-globe-$(VERSION).zip
OPERA_ZIP_MARBLE  := neo-mosaic-opera-marble-$(VERSION).zip

XPI_LATEST_DIAMOND := neo-mosaic-firefox-diamond.xpi
XPI_LATEST_GLOBE   := neo-mosaic-firefox-globe.xpi
XPI_LATEST_MARBLE  := neo-mosaic-firefox-marble.xpi
ZIP_LATEST_DIAMOND := neo-mosaic-chrome-diamond.zip
ZIP_LATEST_GLOBE   := neo-mosaic-chrome-globe.zip
ZIP_LATEST_MARBLE  := neo-mosaic-chrome-marble.zip
OPERA_LATEST_DIAMOND := neo-mosaic-opera-diamond.zip
OPERA_LATEST_GLOBE   := neo-mosaic-opera-globe.zip
OPERA_LATEST_MARBLE  := neo-mosaic-opera-marble.zip

.PHONY: all clean release help

all: $(XPI_LATEST_DIAMOND) $(XPI_LATEST_GLOBE) $(XPI_LATEST_MARBLE) \
     $(ZIP_LATEST_DIAMOND) $(ZIP_LATEST_GLOBE) $(ZIP_LATEST_MARBLE) \
     $(OPERA_LATEST_DIAMOND) $(OPERA_LATEST_GLOBE) $(OPERA_LATEST_MARBLE)

# ------ Firefox -------

$(XPI_LATEST_DIAMOND): $(wildcard firefox/diamond/*)
	cd firefox/diamond && zip -qr ../../$@ *

$(XPI_LATEST_GLOBE): $(wildcard firefox/globe/*)
	cd firefox/globe && zip -qr ../../$@ *

$(XPI_LATEST_MARBLE): $(wildcard firefox/marble/*)
	cd firefox/marble && zip -qr ../../$@ *

# ------ Chrome -------

$(ZIP_LATEST_DIAMOND): $(wildcard chrome/diamond/*)
	cd chrome/diamond && zip -qr ../../$@ *

$(ZIP_LATEST_GLOBE): $(wildcard chrome/globe/*)
	cd chrome/globe && zip -qr ../../$@ *

$(ZIP_LATEST_MARBLE): $(wildcard chrome/marble/*)
	cd chrome/marble && zip -qr ../../$@ *

# ------ Opera GX (Mod format) -------

$(OPERA_LATEST_DIAMOND): $(shell find opera/diamond -type f)
	cd opera/diamond && zip -qr ../../$@ *

$(OPERA_LATEST_GLOBE): $(shell find opera/globe -type f)
	cd opera/globe && zip -qr ../../$@ *

$(OPERA_LATEST_MARBLE): $(shell find opera/marble -type f)
	cd opera/marble && zip -qr ../../$@ *

# ------ Versioned releases -------

release: $(XPI_DIAMOND) $(XPI_GLOBE) $(XPI_MARBLE) \
        $(ZIP_DIAMOND) $(ZIP_GLOBE) $(ZIP_MARBLE) \
        $(OPERA_ZIP_DIAMOND) $(OPERA_ZIP_GLOBE) $(OPERA_ZIP_MARBLE)

$(XPI_DIAMOND): $(XPI_LATEST_DIAMOND)
	cp $< $@

$(XPI_GLOBE): $(XPI_LATEST_GLOBE)
	cp $< $@

$(XPI_MARBLE): $(XPI_LATEST_MARBLE)
	cp $< $@

$(ZIP_DIAMOND): $(ZIP_LATEST_DIAMOND)
	cp $< $@

$(ZIP_GLOBE): $(ZIP_LATEST_GLOBE)
	cp $< $@

$(ZIP_MARBLE): $(ZIP_LATEST_MARBLE)
	cp $< $@

$(OPERA_ZIP_DIAMOND): $(OPERA_LATEST_DIAMOND)
	cp $< $@

$(OPERA_ZIP_GLOBE): $(OPERA_LATEST_GLOBE)
	cp $< $@

$(OPERA_ZIP_MARBLE): $(OPERA_LATEST_MARBLE)
	cp $< $@

# ------ Clean -------

clean:
	rm -f neo-mosaic-*.xpi neo-mosaic-*.zip

# ------ Help -------

help:
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@echo '  all       Build all variant packages (latest unversioned)'
	@echo '  release   Build all variant packages (versioned filenames)'
	@echo '  clean     Remove all build artifacts'
	@echo '  help      Show this message'
	@echo ''
	@echo 'Variables:'
	@echo '  VERSION   Override version (default: from manifest.json)'
	@echo ''
	@echo 'Outputs:'
	@echo '  $(XPI_LATEST_DIAMOND)     Firefox diamond variant (.xpi)'
	@echo '  $(XPI_LATEST_GLOBE)       Firefox globe variant (.xpi)'
	@echo '  $(XPI_LATEST_MARBLE)      Firefox marble variant (.xpi)'
	@echo '  $(ZIP_LATEST_DIAMOND)     Chrome diamond variant (.zip)'
	@echo '  $(ZIP_LATEST_GLOBE)       Chrome globe variant (.zip)'
	@echo '  $(ZIP_LATEST_MARBLE)      Chrome marble variant (.zip)'
	@echo '  $(OPERA_LATEST_DIAMOND)   Opera GX diamond mod (.zip)'
	@echo '  $(OPERA_LATEST_GLOBE)     Opera GX globe mod (.zip)'
	@echo '  $(OPERA_LATEST_MARBLE)    Opera GX marble mod (.zip)'
	@echo ''
	@echo 'Install:'
	@echo '  Firefox:   about:debugging -> Load Temporary Add-on'
	@echo '  Chrome:    chrome://extensions -> Load unpacked'
	@echo '  Opera GX:  opera:extensions -> Load unpacked'
	@echo ''
	@echo 'Example:'
	@echo '  make              # build latest'
	@echo '  make release      # build with version in filename'
	@echo '  make clean        # remove packages'
