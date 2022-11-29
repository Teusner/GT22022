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

presentation: $(PRESENTATION_BUILD_DIR)/presentation.pdf manim videos

$(PRESENTATION_BUILD_DIR)/presentation.pdf: src/presentation.tex
	$(dir_guard)
	latexmk -pdfxe -shell-escape -output-directory=$(PRESENTATION_BUILD_DIR) $<

# Manim
MANIM_SOURCES := $(filter-out scripts/frame.py, $(wildcard scripts/*.py))
MANIM_ANIMATIONS = $(MANIM_SOURCES:scripts/%.py=%.mp4)
MANIM_THUMBNAILS = $(MANIM_SOURCES:scripts/%.py=%.png)
manim: $(addprefix $(PRESENTATION_BUILD_DIR)/, ${MANIM_ANIMATIONS}) $(addprefix $(IMGS_BUILD_DIR)/manim/, ${MANIM_THUMBNAILS})

$(PRESENTATION_BUILD_DIR)/%.mp4 : scripts/%.py
	$(dir_guard)
	manim -qh -r 1024,1024 $< $*
	cp -f build/manim/videos/$*/1024p60/$*.mp4 $@

$(IMGS_BUILD_DIR)/manim/%.png : $(PRESENTATION_BUILD_DIR)/%.mp4
	$(dir_guard)
	ffmpeg -i $< -ss 00:00:09.000 -vframes 1 $@

# Videos
VIDEOS_SOURCES = $(wildcard videos/*.mp4)
VIDEOS_NAMES = $(VIDEOS_SOURCES:videos/%.mp4=%.mp4)
VIDEOS_THUMBNAIL = $(VIDEOS_SOURCES:videos/%.mp4=%.png)
videos: $(addprefix $(PRESENTATION_BUILD_DIR)/, ${VIDEOS_NAMES}) $(addprefix $(IMGS_BUILD_DIR)/videos/, ${VIDEOS_THUMBNAIL})

$(PRESENTATION_BUILD_DIR)/%.mp4 : videos/%.mp4
	$(dir_guard)
	ln $< $@

$(IMGS_BUILD_DIR)/videos/%.png : videos/%.mp4
	$(dir_guard)
	ffmpeg -i $< -ss 00:00:05.000 -vframes 1 $@

# Clean recipe
clean:
	rm -rf $(BUILD_DIR)