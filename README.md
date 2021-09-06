[![GitHub Actions status](https://github.com/jordimas/tmx-to-text/workflows/Tests/badge.svg)](https://github.com/jordimas/tmx-to-text/actions)
[![PyPI version](https://img.shields.io/pypi/v/tmx-to-text.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/tmx-to-text/)
[![PyPI downloads](https://img.shields.io/pypi/dm/tmx-to-text.svg)](https://pypistats.org/packages/tmx-to-text)


# Introduction

tmx-to-text allows convert TMX files into plain text.

The following command will extract the Catalan and Italian texts out of the TMX file:

```
tmx-to-text.py -f ca-it.tmx -s ca -t it
```

Running the application with *-h* shows the options avaiable

```
Converts TMX into two text files
Usage: tmx-to-text [options]

Options:
  -h, --help            show this help message and exit
  -f TMX_FILE, --tmx-file=TMX_FILE
                        tmx File to convert to Text
  -s SOURCE_LANGUAGE, --source_lang=SOURCE_LANGUAGE
                        Source text file
  -t TARGET_LANGUAGE, --target_lang=TARGET_LANGUAGE
                        Target text file
  -p PREFIX, --prefix=PREFIX
                        Filename prefix
```

