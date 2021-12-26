from PIL import Image, ImageOps
import numpy as np
import pytesseract

def negate(filename):
    img = Image.open(filename).convert('L')
    imgNeg = ImageOps.invert(img)
    return imgNeg

def toNumpy(img) -> np.array:
    arr = np.asarray(img)
    return arr

if __name__ == "__main__":
    img = negate(input())
    arr = toNumpy(img)
    arr =arr.copy()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # print(arr[i,j])
            if arr[i,j] < 35:
                arr[i,j]=0
            else:
                arr[i,j]=255
    img = Image.fromarray(arr)
    img.save("new.jpeg")
    text = pytesseract.image_to_string(img, lang="eng")
    # print(text)
    i = len(text)-1
    while text[i]=='\n' or text[i]=='\f':
        i-=1
    print(text[:i+1])