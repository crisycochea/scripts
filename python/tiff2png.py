#!/home/cris/scripts/python/.venv/bin/python

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import logging
import os

from PIL import Image

CURRENT_PATH = os.path.abspath(os.getcwd())
def to_png():
    filename = sys.argv[1]
    filename_without_extension = filename.split('.')[0]
    file_path = os.path.join(CURRENT_PATH, filename)
    image: Image.Image = Image.open(file_path)
    new_filename = filename_without_extension + '.png'
    new_path = os.path.join(CURRENT_PATH, new_filename)
    image.convert(mode="RGB").save(new_path)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    to_png()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
