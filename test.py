# imgmin
# A simple api to create minified images
# Github: https://www.github.com/0x4248/imgmin
# License: GNU General Public License v3.0
# By: 0x4248
#
# Test script for imgmin that downloads an image and minifies it

import requests
import imgmin

# Download example image
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/SMPTE_Color_Bars.svg/2560px-SMPTE_Color_Bars.svg.png"

r = requests.get(url, allow_redirects=True)
open("test.png", "wb").write(r.content)

# Minify the image
imgmin.generate_minified_images("test.png")
