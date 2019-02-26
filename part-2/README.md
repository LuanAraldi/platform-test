# Platform test Part 2/2

This part of the test consists in a dump generator based in a input dump

It was built using Python 3.6 to take advantage of its high performance and fast file manipulation

## Prerequisites

- [Python 3.6]{https://www.python.org/downloads/release/python-367/}

## Pre-setup

Install required packages with
```bash
pip3 install -r requirements.txt
```

## Run tests

```bash
python3 test.py
```

## Run application

To run the application it's necessary to specify an the compacted input dump, just like the example below
```bash
python3 init.py dump_file.tar.gz
```

It will generate a dump.json file in the directory the script is being called with the generated dump file.