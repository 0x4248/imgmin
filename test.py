# imgmin
# A simple api to create minified images
# Github: https://www.github.com/lewisevans2007/imgmin
# License: GNU General Public License v3.0
# By: Lewis Evans

import requests
import imgmin

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/SMPTE_Color_Bars.svg/2560px-SMPTE_Color_Bars.svg.png"

r = requests.get(url, allow_redirects=True)
open('test.png', 'wb').write(r.content)

imgmin.generate_minified_images("test.png")