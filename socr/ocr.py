from subprocess import check_output
from subprocess import call
from shlex import quote


def size_up(original_file, temp_file):
    call((
        'convert', 
        original_file, 
        '-units', 'pixelsperinch', 
        '-resample', '300',
        '-colorspace', 'gray',
        '-depth', '2',
        temp_file
    ))


def recognise(temp_file):
    return check_output((
        'tesseract',
        temp_file,
        'stdout'
    ))


def embed(text, original_file):
    call((
        'exiftool',
        '-overwrite_original_in_place', 
        f'-description={quote(text)}',
        original_file,
        '-execute'
    ))
