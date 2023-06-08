import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Load the image
image_path = 'doc.jpg'
image = Image.open(image_path)

# Extract the text from the image
text = pytesseract.image_to_string(image)
# Split the extracted text into individual words
words = text.lower().split()

if "math" in words and "master" in words:
    print("eligible for bachleor teaching")
if "Nepali" in words and "bachleor" in words:
    print("eligible for 11 12 teaching")
if "social" in words and "+2" in words:
    print("eligible for school teching")
if "Science" in words and "master" in words:
    print("eligible for bachleor teaching")
if "Computer" in words and "bachleor" in words:
    print("eligible for 11 12 teaching")
if "Health & Population" in words and "+2" in words:
    print("eligible for school teching")
else:
    print("not eligible")
