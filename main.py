import pytesseract
import cv2
import os
from PIL import Image, ImageEnhance

# to do
# 1. image pre-processing before text extraction
# 2. text cleaning after text extraction
def extract_text_from_image(file_path: str)->str:
    
    # read image
    img = Image.open(file_path)

    # convert to grayscale
    gray = img.convert('L')

    #image resizing
    img = resize_images(gray)

    # image brightness and contrast adjustment
    img = image_brightness_contrast(img)

    # config
    config = ('-l eng --oem 1 --psm 3')

    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # images to text
    text = pytesseract.image_to_string(img, config=config)

    return text

def resize_images(image, min_height=40, min_width=20):
    width, height = image.size

    if height < 300:
        scale_ftr = 300 / height
    elif height > 2000:
        scale_ftr = 1200 / height
    else:
        scale_ftr = 1.0

    if scale_ftr != 1.0:
        new_width = int(width * scale_ftr)
        new_height = int(height * scale_ftr)
        res_img = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        print(f"old size: {width}x{height}, new size: {new_width}x{new_height}")
    else:
        res_img = image
        print(f"Image size is already optimal: {width}x{height}")

    return res_img

def image_brightness_contrast(image, brightness=1.1, contrast=1.1):
    bright = ImageEnhance.Brightness(image)
    bright_img = bright.enhance(brightness)

    cont = ImageEnhance.Contrast(bright_img)
    cont_img = cont.enhance(contrast)

    return cont_img

if __name__ == "__main__":
    print("SafeEats is running...\n\n")
    imgs = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.webp', 'img5.jpg', 'img6.webp', 'img7.jpg']
    
    imgs_dir = os.path.join(os.path.dirname(__file__), "test_images")
    for img in imgs:
        pth = os.path.join(imgs_dir, img)
        text = extract_text_from_image(pth)
        print(f"Extracted text from {img}:")
        print(text)
        print("\n\n")