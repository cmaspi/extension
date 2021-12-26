import numpy as np
from PIL import Image, ImageOps

def negate(filename):
    img = Image.open(filename).convert('L')
    imgNeg = ImageOps.invert(img)
    imgNeg.save("result.jpeg")

if __name__ == "__main__":
    negate("78kkn.jpeg")