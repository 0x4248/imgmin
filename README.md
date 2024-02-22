# Imgmin

A simple api to create minified images

## Usage

### minify_image

Minifies an image by a certain amount of times
It will take in the input of the image and output name.min.extension

#### Args
- image_path (str): the path to the image
- times (int, optional): How many times to shrink the image. e.g if 2 then output will be 2 times smaller. Defaults to 2.

#### Returns
- str: the path to the minified image

### generate_minified_images

Generates 4 minified images from the original image
1. 2x smaller
2. 4x smaller
3. 6x smaller
4. 8x smaller

#### Args

- image_path (str): the path to the image

#### Returns
- list: a list of the paths to the minified images


## Licence

This project is licensed under the GNU General Public License v3.0 - see the [LICENCE](LICENCE) file for details