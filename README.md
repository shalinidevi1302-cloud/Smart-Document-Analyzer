# Smart Document Analyzer
app:http://localhost:8501/
A Python-based OCR application that extracts and analyzes information from document images using Tesseract OCR, OpenCV, and Streamlit.

## Features

- Upload PNG, JPG, and JPEG documents
- Image preprocessing using OpenCV
- Text extraction using Tesseract OCR
- Automatic extraction of important information
- Document summary generation
- Downloadable analysis report
- Simple Streamlit web interface

## Technologies Used

- Python
- Streamlit
- Tesseract OCR
- Pytesseract
- OpenCV
- Pillow
- Regular Expressions

## Project Structure

```text
Smart-Document-Analyzer/
│
├── app.py
├── ocr.py
├── preprocessing.py
├── analyzer.py
├── requirements.txt
├── README.md
├── .gitignore
└── test_image.png
How to Run
1. Clone the Repository
git clone https://github.com/your-username/Smart-Document-Analyzer.git
cd Smart-Document-Analyzer
2. Create Virtual Environment
python -m venv venv
3. Activate Virtual Environment
venv\Scripts\Activate.ps1
4. Install Dependencies
pip install -r requirements.txt
5. Install Tesseract OCR

Install Tesseract OCR on your system.

Default Windows path used in this project:

C:\Program Files\Tesseract-OCR\tesseract.exe
6. Run the Application
streamlit run app.py

The application will open in the browser.

Example
Input
SMART DOCUMENT ANALYZER

Name: Shalini Devi
College: ABC College
Course: B.Sc Computer Science
Amount: Rs. 25000
Date: 05-10-2026
Output
Name: Shalini Devi
College: ABC College
Course: B.Sc Computer Science
Amount: Rs. 25000
Date: 05-10-2026

The application also generates a document summary and allows the user to download the analysis report.

Use Cases
Student documents
Receipts
Invoices
Certificates
Forms
Bills
Business documents
Future Enhancements
PDF report generation
AI/LLM integration
Handwritten text recognition
Multi-language OCR
PDF input support
Database integration
Cloud deployment
Author

Shalini Devi

B.Sc Computer Science with AI
