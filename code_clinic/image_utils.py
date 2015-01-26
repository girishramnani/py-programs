from PIL import Image

__author__ = 'Girish'
import PIL.ExifTags


def get_image_data(image):

    img = Image.open(image)
    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    return exif

