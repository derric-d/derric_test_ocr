#!/bin/bash/python3
"""
python ocr test script
test data lives in /home/derric/code/tessdata/end.traineddata
"""
try:
    from PIL import Image, ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = True
except ImportError:
    import Image, ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = True
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

text = pytesseract.image_to_string(Image.open('helloworld.jpeg'), lang='eng')

print(text)
