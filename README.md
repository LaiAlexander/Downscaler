# Downscaler
A script to downscale images to reduce size for mail, web etc

Default size is width/2 and height/2 or 25% of the original size.
`FACTOR` may be edited if another size is what you want.

## Usage
Simply drag and drop the image file onto the script file. A new image will be saved in the same folder as the original image. The name of the new image will be [original-name]-resized.extension. Multiple images is supported,
just select them all and drag-drop them onto the script.

## Requirements
[pillow](https://python-pillow.org/)

Install with PyPI: `pip install pillow`