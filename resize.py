from PIL import Image
import os
import glob


def resize(image):
    im = Image.open(image)
    rgb_im = im.convert('RGB')
    im1 = rgb_im.resize((1200, 1500))
    name = "1" + image[2:]
    im1.save(name)
    os.remove(image)


