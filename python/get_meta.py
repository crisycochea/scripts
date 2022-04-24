#!/home/cris/scripts/python/.venv/bin/python

import sys
import logging
import os

from PIL import ExifTags, Image, TiffTags
from PIL.ExifTags import TAGS
from PIL.TiffImagePlugin import ImageFileDirectory_v1

CURRENT_PATH = os.path.abspath(os.getcwd())


def get_meta():
    filename = sys.argv[1]
    file_path = os.path.join(CURRENT_PATH, filename)
    image: Image.Image = Image.open(file_path)
    # image: Image.Image = Image.open('/home/cris/Documentos/puccasky/ecuaciones/02_Imagenes/02_Banda2_Abril2013.tif')
    # exifdata = image.getexif()
    tag: ImageFileDirectory_v1 = image.tag
    for key, val in tag.items():
        if key in TiffTags.TAGS:
            print(f'{TiffTags.TAGS[key]}:{val}\n')
    # exif = { ExifTags.TAGS[k]: v for k, v in image.getexif().items() if k in ExifTags.TAGS }
    # for id in image.tag:
    #     print("{} : {}".format(id, image.tag[id]))
    # print(image.tag)
    # for tag_id in exifdata:
    #     # get the tag name, instead of human unreadable tag id
    #     print(tag_id)
    #     tag = TAGS.get(tag_id, tag_id)
    #     data = exifdata.get(tag_id)
    #     if isinstance(data, bytes):
    #         data = data.decode()
    #     print(f"{tag:25}: {data}")


if __name__ == '__main__':
    get_meta()

