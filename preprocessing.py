import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Remove noise
    denoised = cv2.GaussianBlur(gray, (5, 5), 0)

    # Improve text visibility
    threshold = cv2.threshold(
        denoised, 0, 255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return threshold