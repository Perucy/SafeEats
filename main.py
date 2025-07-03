import pytesseract
import cv2
import PIL

# to do
# 1. image pre-processing before text extraction
# 2. text cleaning after text extraction
def extract_text_from_image(file_path: str)->str:
    
    # read image
    img = cv2.imread(file_path)

    # config
    config = ('-l eng --oem 1 --psm 3')

    #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # images to text
    text = pytesseract.image_to_string(img, config=config)

    return text
if __name__ == "__main__":
    print("SafeEats is running...")
    imgs = ['img1.jpg', 'img2.jpg', 'img3.jpg', 'img4.webp', 'img5.jpg', 'img6.webp', 'img7.jpg']
    
    for img in imgs:
        
        pth = f"/Users/perucymussiba/Desktop/projects/SafeEats/test_images/{img}"
        text = extract_text_from_image(pth)
        print(f"Extracted text from {img}:")
        print(text)
        print("\n\n")