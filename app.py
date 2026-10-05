import streamlit as st
import pytesseract
from PIL import Image

from preprocessing import preprocess_image
from analyzer import analyze_text, generate_summary

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


st.set_page_config(
    page_title="Smart Document Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Smart Document Analyzer")
st.write("Upload a document image to extract and analyze information.")

uploaded_file = st.file_uploader(
    "Upload your document",
    type=["png", "jpg", "jpeg"]
)


if uploaded_file is not None:

    # Display uploaded image
    image = Image.open(uploaded_file)

    st.subheader("📷 Uploaded Document")
    st.image(image, use_container_width=True)

    # Save uploaded image temporarily
    image_path = "uploaded_document.png"
    image.save(image_path)

    # Preprocessing
    processed_image = preprocess_image(image_path)

    # OCR
    text = pytesseract.image_to_string(processed_image)

    # Display extracted text
    st.subheader("🔍 Extracted Text")
    st.text_area(
        "OCR Result",
        text,
        height=200
    )

    # Analyze
    result = analyze_text(text)

    st.subheader("🧠 Document Analysis")

    summary = generate_summary(result)

st.subheader("📝 Document Summary")

st.write(summary)
# Create report
report = f"""
SMART DOCUMENT ANALYZER
=======================

EXTRACTED TEXT
--------------
{text}

DOCUMENT ANALYSIS
-----------------
"""

for key, value in result.items():
    report += f"{key}: {value}\n"

report += f"""
DOCUMENT SUMMARY
----------------
{summary}
"""

st.download_button(
    label="⬇️ Download Report",
    data=report,
    file_name="smart_document_report.txt",
    mime="text/plain"
)