"""
A script to automate resizing of images.
Simply drag and drop the image onto the script file
and a new, resized image will be saved in the same folder as the original image.
The new image will be named originalname-resized.extension.
"""

import os
import sys
from PIL import Image

FACTOR = 2

def make_savename(filepath):
    """
    Adds "-resized" before the file extension and returns the string.
    Will work even if the filename contains periods.

    :Args:
    `filepath` is the full path of the image to resize

    :Returns:
    The new properly formatted string.
    """
    filepath = filepath.split(os.sep)
    filename = filepath[-1].split(".") # Split into list, so we can pop off last element
    ext = filename.pop() # Both removes last element(extension) and saves the extension for later
    filename = ".".join(filename) # Joining name of file
    filename = filename + "-resized." + ext
    filepath[-1] = filename
    filepath = os.sep.join(filepath)
    return filepath

def downscale(filepath, factor):
    """
    Scales down an image and saves the new image in the same folder with a new name.

    :Args:
    `filepath` is the path of the image to be resized.
    `factor` is the resizing factor.
    Width and height of the image will be divided by `factor`.
    """
    try:
        img = Image.open(filepath)
    except OSError:
        print("Not valid file format.")
        return
    except Exception as exc:
        print(exc)
        input("Something went wrong when opening image. Press enter to quit script.")
        return

    # Resize image
    new_width = int(img.size[0] / factor)
    new_height = int(img.size[1] / factor)
    img = img.resize((new_width, new_height), Image.ANTIALIAS)

    # Should be possible to use the following as well,
    # but first separator after drive letter is missing on Windows for some
    # filepath = os.path.join(*filepath))

    try:
        img.save(make_savename(filepath), quality=95)
    except Exception as exc:
        print(exc)
        print(filepath)
        input("Something went wrong while trying to save. Press enter to quit script.")

def main(argv):
    """
    Main function
    """
    if len(argv) > 1:
        argv.pop(0)
        for filepath in argv:
            downscale(filepath, FACTOR)
    else:
        print("Drag and drop the image to be resized on top of this file.")
    # if len(argv) > 1:
    #     filepath = argv[1]
    #     downscale(filepath, FACTOR)
    # else:
    #     print("Drag and drop the image to be resized on top of this file.")

main(sys.argv)
