# socr
screenshot OCR tool, allows you to keep a searchable database of your screenshots and their contained text

```
Usage: socr [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  add     add a single screenshot to the database
  build   build db from the directory (run once)
  search  search for a screenshot given text
```

# requirements 
  - [imagemagick](https://www.imagemagick.org/script/index.php)
  - [tesseract](https://github.com/tesseract-ocr/tesseract)
  - [exiftool](https://www.sno.phy.queensu.ca/~phil/exiftool/)
  - probably linux
  
# setup
  - `pip3 install --user git+https://github.com/sentriz/socr.git`
  - `edit ~/.config/socr/config.py` see example config
  - `socr build` run once per install. looks at all your screenshots, extracts the text, embeds the text, and builds the database
  - add `socr add <path to screenshot>` to [your screenshoting tool](https://github.com/sentriz/dotfiles/commit/57987138e4b09615b8237b6ac67e4d751dfbabb1)

# example usage
  - `socr search <text>` to see matching files
  - `feh $(socr search <text>)` with, for example, [feh](https://wiki.archlinux.org/index.php/Feh) too view all matching screenshots
  - `rm $(socr search <secret>)` to delete screenshots with matching text (say you captured your password accidentally)
  
# example config
```python
# ~/.config/socr/config.py

SCREENSHOT_DIR="~/pictures/screenshots"
SCREENSHOT_EXT="png"
```
