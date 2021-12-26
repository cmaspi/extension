import numpy as np
from PIL import Image
import pytesseract
def toNumpy(filename) -> np.array:
    img = Image.open(filename).convert('L')
    arr = np.asarray(img)
    return arr

if __name__ == "__main__":
    arr = toNumpy("result.jpeg")
    arr =arr.copy()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            # print(arr[i,j])
            if arr[i,j] < 40:
                arr[i,j]=0
            else:
                arr[i,j]=255
    img = Image.fromarray(arr)
    # img.save("seeThis.jpeg")
    text = pytesseract.image_to_string(img, lang="eng")
    print(text)

