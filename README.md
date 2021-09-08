[![GitHub Actions status](https://github.com/jordimas/tmx-to-text/workflows/Tests/badge.svg)](https://github.com/jordimas/tmx-to-text/actions)
[![PyPI version](https://img.shields.io/pypi/v/tmx-to-text.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/tmx-to-text/)
[![PyPI downloads](https://img.shields.io/pypi/dm/tmx-to-text.svg)](https://pypistats.org/packages/tmx-to-text)


# Introduction

tmx-to-text allows convert TMX files into plain text and to get information.

This tool be used for example to:
* Extract translations memories into text file for spell checking or post-editing
* Extract corpuses into text files for traning machine learning similar

The following command will extract the Catalan and Italian texts out of the TMX file:

```
tmx-to-text convert -f ca-it.tmx -s ca -t it
```

Running the application with *-h* shows the options avaiable for the info and convert commands.

```
usage: tmx-to-text info [-h] -f TMX_FILE

optional arguments:
  -h, --help   show this help message and exit
  -f TMX_FILE  TMX file to show info


usage: tmx-to-text convert [-h] -f TMX_FILE -s SOURCE_LANG -t TARGET_LANG [-p PREFIX] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -f TMX_FILE           TMX file to convert
  -s SOURCE_LANG, --source_lang SOURCE_LANG
                        Source language to export
  -t TARGET_LANG, --target_lang TARGET_LANG
                        Target language to export
  -p PREFIX, --prefix PREFIX
                        Filename prefix used in the generated text files
  -d, --debug           Debug memory and execution time
 Debug memory and execution time

```

