VERSION ?= $(shell python3 -c "import json; print(json.load(open('firefox/diamond/manifest.json'))['version'])")

XPI_DIAMOND   := neo-mosaic-firefox-diamond-$(VERSION).xpi
XPI_GLOBE     := neo-mosaic-firefox-globe-$(VERSION).xpi
ZIP_DIAMOND   := neo-mosaic-chrome-diamond-$(VERSION).zip
ZIP_GLOBE     := neo-mosaic-chrome-globe-$(VERSION).zip

XPI_LATEST_DIAMOND := neo-mosaic-firefox-diamond.xpi
XPI_LATEST_GLOBE   := neo-mosaic-firefox-globe.xpi
ZIP_LATEST_DIAMOND := neo-mosaic-chrome-diamond.zip
ZIP_LATEST_GLOBE   := neo-mosaic-chrome-globe.zip

.PHONY: all clean release help

all: $(XPI_LATEST_DIAMOND) $(XPI_LATEST_GLOBE) $(ZIP_LATEST_DIAMOND) $(ZIP_LATEST_GLOBE)

# ------ Firefox -------

$(XPI_LATEST_DIAMOND): $(wildcard firefox/diamond/*)
	cd firefox/diamond && zip -qr ../../$@ *

$(XPI_LATEST_GLOBE): $(wildcard firefox/globe/*)
	cd firefox/globe && zip -qr ../../$@ *

# ------ Chrome -------

$(ZIP_LATEST_DIAMOND): $(wildcard chrome/diamond/*)
	cd chrome/diamond && zip -qr ../../$@ *

$(ZIP_LATEST_GLOBE): $(wildcard chrome/globe/*)
	cd chrome/globe && zip -qr ../../$@ *

# ------ Versioned releases -------

release: $(XPI_DIAMOND) $(XPI_GLOBE) $(ZIP_DIAMOND) $(ZIP_GLOBE)

$(XPI_DIAMOND): $(XPI_LATEST_DIAMOND)
	cp $< $@

$(XPI_GLOBE): $(XPI_LATEST_GLOBE)
	cp $< $@

$(ZIP_DIAMOND): $(ZIP_LATEST_DIAMOND)
	cp $< $@

$(ZIP_GLOBE): $(ZIP_LATEST_GLOBE)
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
	@echo '  $(XPI_LATEST_DIAMOND)     Firefox diamond variant'
	@echo '  $(XPI_LATEST_GLOBE)       Firefox globe variant'
	@echo '  $(ZIP_LATEST_DIAMOND)     Chrome diamond variant'
	@echo '  $(ZIP_LATEST_GLOBE)       Chrome globe variant'
	@echo ''
	@echo 'Example:'
	@echo '  make              # build latest'
	@echo '  make release      # build with version in filename'
	@echo '  make clean        # remove packages'
