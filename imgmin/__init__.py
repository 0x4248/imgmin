# imgmin
# A simple api to create minified images
# Github: https://www.github.com/lewisevans2007/imgmin
# License: GNU General Public License v3.0
# By: Lewis Evans

import os
from PIL import Image

__all__ = ["minify_image", "generate_minified_images"]

def minify_image(image_path, times=2):
    """Minifies an image by a certain amount of times
    It will take in the input of the image and output name.min.extension

    Args:
        image_path (str): The path to the image
        times (int, optional): How many times to shrink the image. e.g if 2 then output will be 2 times smaller. Defaults to 2.
    Returns:
        str: The path to the minified image
    """
    image_name = os.path.basename(image_path)
    image_extension = os.path.splitext(image_name)[1]

    image = Image.open(image_path)
    image_size = image.size

    new_size = (image_size[0] // times, image_size[1] // times)
    image = image.resize(new_size)

    image.save(f"{os.path.splitext(image_path)[0]}.min{image_extension}")

    return f"{os.path.splitext(image_path)[0]}.min{image_extension}"


def generate_minified_images(image_path):
    """Generates 4 minified images from the original image
    1. 2x smaller
    2. 4x smaller
    3. 6x smaller
    4. 8x smaller
    Args:
        image_path (str): The path to the image
    Returns:
        list: A list of the paths to the minified images
    """
    image_name = os.path.basename(image_path)
    image_extension = os.path.splitext(image_name)[1]

    image = Image.open(image_path)
    image_size = image.size

    new_size_1 = (image_size[0] // 2, image_size[1] // 2)
    new_size_2 = (image_size[0] // 4, image_size[1] // 4)
    new_size_3 = (image_size[0] // 6, image_size[1] // 6)
    new_size_4 = (image_size[0] // 8, image_size[1] // 8)

    image_1 = image.resize(new_size_1)
    image_2 = image.resize(new_size_2)
    image_3 = image.resize(new_size_3)
    image_4 = image.resize(new_size_4)

    image_1.save(f"{os.path.splitext(image_path)[0]}.min1{image_extension}")
    image_2.save(f"{os.path.splitext(image_path)[0]}.min2{image_extension}")
    image_3.save(f"{os.path.splitext(image_path)[0]}.min3{image_extension}")
    image_4.save(f"{os.path.splitext(image_path)[0]}.min4{image_extension}")

    return [
        f"{os.path.splitext(image_path)[0]}.min1{image_extension}",
        f"{os.path.splitext(image_path)[0]}.min2{image_extension}",
        f"{os.path.splitext(image_path)[0]}.min3{image_extension}",
        f"{os.path.splitext(image_path)[0]}.min4{image_extension}",
    ]
