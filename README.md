# Word Filter

## Overview

Word Filter is a simple utility that provides a list of words that contain a specified substring 
and sample paragraphs with those words in context.

## Features

The script takes a text corpus in the format of text corpora provided by the Leipzig Corpora Collection. 
Specifically, the files expected are a directory containing files with similar names, with words 
and sentences to parse. The words file is a list of tab-separated frequency, word pairs with one word 
per line, sorted first in descrnding order of frequency, then in alphabetical order. The sentences 
file contains one sentence per line. If no files are specified, a dfault.txt file could be defined with 
a list of sentences to be parsed and used instead.

To get started, clone this repository and make sure to have python3 and/or a python environment active.
to run the script, use the command:

```python word-filter.py [arguments]```

### The following arguments are accepted:

- `-f, --files`: The directory of corpus files (.txt) located in a ```data``` folder in the same directory as the script.
- `-s, --substring`: (required) The substring words should contain.
- `-c, --count`: The number of words to find.
- `-p, --print-sample`: (flag, false by default) Whether to provide a paragraph with the found words in an artificial context.

An example use is as follows, specifying 10-length lists of words containing the substring "ción", 
along with a sample paragraph, in the "data/default.txt" file:

```python word-filter.py -s ción -c 10 -p```
