import pytesseract

from preprocessing import preprocess_image
from analyzer import analyze_text


# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Image path
image_path = "test_image.png"


# Step 1: Preprocess image
processed_image = preprocess_image(image_path)


# Step 2: Extract text using OCR
text = pytesseract.image_to_string(processed_image)


print("========== EXTRACTED TEXT ==========")
print(text)
print("====================================")


# Step 3: Analyze extracted text
result = analyze_text(text)


print("\n========== DOCUMENT ANALYSIS ==========")

for key, value in result.items():
    print(f"{key}: {value}")

print("=======================================")