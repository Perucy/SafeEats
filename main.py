import pytesseract
import cv2
import os
from PIL import Image

# to do
# 1. image pre-processing before text extraction
# 2. text cleaning after text extraction
def extract_text_from_image(file_path: str)->str:
    
    # read image
    img = Image.open(file_path)

    # convert to grayscale
    gray = img.convert('L')

    # config
    config = ('-l eng --oem 1 --psm 3')

    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # images to text
    text = pytesseract.image_to_string(img, config=config)

    return text
if __name__ == "__main__":
    print("SafeEats is running...")
    imgs = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.webp', 'img5.jpg', 'img6.webp', 'img7.jpg']
    
    imgs_dir = os.path.join(os.path.dirname(__file__), "test_images")
    for img in imgs:
        pth = os.path.join(imgs_dir, img)
        text = extract_text_from_image(pth)
        print(f"Extracted text from {img}:")
        print(text)
        print("\n\n")