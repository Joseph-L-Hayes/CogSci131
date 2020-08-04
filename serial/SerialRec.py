try:
    from PIL import Image

except ImportError:
    import Image

import pytesseract

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))

    return text


print(ocr_core('images/ocr_example_2.jpg'))
