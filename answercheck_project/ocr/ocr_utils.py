import pytesseract
from PIL import Image
from io import BytesIO

def process_image(image_file):
    """
    This function receives an image file, applies OCR, and returns the extracted text.
    """
    img = Image.open(image_file)
    # Convert the image to text using Tesseract
    text = pytesseract.image_to_string(img)
    return text
