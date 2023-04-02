import cv2


img_path='test.jpeg'
img = cv2.imread(img_path)

from PIL import Image
from pytesseract import *
import re

img=Image.open(img_path)

text= pytesseract.image_to_string(img)

print(text)




