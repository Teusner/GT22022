# Directory configuration
BUILD_DIR = build
ABSTRACT_DIR = abstract
PRESENTATION_DIR = presentation
ARTICLE_DIR = article
IMGS_DIR = imgs
VIDEOS_DIR = videos

# Directory path combining
ABSTRACT_BUILD_DIR = $(BUILD_DIR)/$(ABSTRACT_DIR)
PRESENTATION_BUILD_DIR = $(BUILD_DIR)/$(PRESENTATION_DIR)
ARTICLE_BUILD_DIR = $(BUILD_DIR)/$(ARTICLE_DIR)
IMGS_BUILD_DIR = $(BUILD_DIR)/$(IMGS_DIR)

# TEX sources
TEX_SRCS := $(wildcard */*.tex)

# Directory guard
dir_guard = @mkdir -p $(@D)

# All recipe
all: abstract presentation

### Numeric reports
# Abstract
abstract: $(ABSTRACT_BUILD_DIR)/abstract.pdf

$(ABSTRACT_BUILD_DIR)/abstract.pdf: src/abstract.tex
	$(dir_guard)
	latexmk -pdf -shell-escape -output-directory=$(ABSTRACT_BUILD_DIR) $<

presentation: $(PRESENTATION_BUILD_DIR)/presentation.pdf manim

$(PRESENTATION_BUILD_DIR)/presentation.pdf: src/presentation.tex
	$(dir_guard)
	latexmk -pdfxe -shell-escape -output-directory=$(PRESENTATION_BUILD_DIR) $<

# Manim
MANIM_SOURCES := $(filter-out scripts/frame.py, $(wildcard scripts/*.py))
MANIM_ANIMATIONS = $(MANIM_SOURCES:scripts/%.py=%.mp4)
manim: $(addprefix $(PRESENTATION_BUILD_DIR)/, ${MANIM_ANIMATIONS})

$(PRESENTATION_BUILD_DIR)/%.mp4 : scripts/%.py
	$(dir_guard)
	manim -qh -r 1000,1000 $< $*
	cp -f build/manim/videos/$*/1000p60/$*.mp4 $@

# Clean recipe
clean:
	rm -rf $(BUILD_DIR)