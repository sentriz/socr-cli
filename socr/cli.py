#!/usr/bin/env python3

import click 
import sys
import os

from socr import files
from socr import ocr
from socr import paths


@click.group()
def cli():
    pass


@cli.command()
@click.argument('path', 
                type=click.Path(exists=True))
def add(path):
    '''add a single screenshot to the database'''
    ocr.size_up(path, paths.TEMP_FILE)
    raw_text = ocr.recognise(paths.TEMP_FILE)
    text = raw_text.decode("utf-8")
    if not text:
        return
    ocr.embed(text, path)
    files.add_scrot(path, text)


@cli.command()
def build():
    '''build db from the directory (run once)'''
    files.write_pickle(files.read_files())


@cli.command()
@click.argument('query')
def search(query):
    '''search for a screenshot given text'''
    for filename, text in files.read_pickle():
        if not text:
            continue
        if not query.lower() in text.lower():
            continue
        path = os.path.join(paths.SCREENSHOT_DIR, filename)
        print(os.path.abspath(path))


if __name__ == '__main__':
    cli() 
