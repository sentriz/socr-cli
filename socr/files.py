#!/usr/bin/env python3

import glob
import pickle
import re
import subprocess 
import sys
import os

import socr.paths as paths


def parse_exif(raw_data):
    data = raw_data.decode("utf-8")
    match = re.match(r'^Description\s+:\s(.*)\n$', data)
    if match:
        return match.group(1)


def get_description(filename):
    result = subprocess.check_output(['exiftool', '-description', filename])
    return parse_exif(result)


def read_files(pattern=paths.SCROT_PATTERN, pickle_path=paths.PICKLE_PATH):
    for screenshot in glob.glob(pattern):
        yield screenshot, get_description(screenshot)


def write_pickle(pics, pickle_path=paths.PICKLE_PATH):
    with open(pickle_path, 'wb') as handle:
        pickle.dump(pics, handle, protocol=pickle.HIGHEST_PROTOCOL)


def read_pickle(pickle_path=paths.PICKLE_PATH):
    with open(pickle_path, 'rb') as handle:
        return pickle.load(handle)


def add_scrot(filename, text):
    pics = read_pickle()
    pics.append((filename, text))
    write_pickle(pics)
