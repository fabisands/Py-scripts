# Install first the libraries pillow and tesseract using "pip install tesseract", "pip install pytesseract" and "pip install pillow"

import pytesseract
from PIL import Image # "PIL" for library "pillow"

# Path to Tesseract executable
# You may need to specify the full path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
# You may need to specify the full path
image_path = r'C:\Users\faren\OneDrive - Universidad de la Amazonia\Pictures\JD_01.jpg'
image = Image.open(image_path)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Define the output text file name
output_file = "extracted_text.txt"

# Save the extracted text to a text file
with open(output_file, "w", encoding="utf-8") as text_file:
    text_file.write(extracted_text)

print("Text extracted and saved to:", output_file)
