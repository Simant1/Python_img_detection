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
 
 #for math subject
if "math" in words and "master" in words: 
    print("eligible for bachleor teaching")

if "math" in words and "bachelor" in words: 
    print("eligible for +2 teaching")


#nepali
if "Nepali" in words and "bachleor" in words:
    print("eligible for 11 12 teaching")
if "Nepali" in words and "master" in words:
    print("eligible for Bachelor teaching")

#for social
if "social" in words and "master" in words:
    print("eligible for bachelor teching")
if "social" in words and "bachleor" in words:
    print("eligible for 11 12 teaching")

#for Science 
if "Science" in words and "master" in words:
    print("eligible for Bachelor teching")
if "Science" in words and "bachleor" in words:
    print("eligible for 11 12 teaching")

#for computer
if "computer" in words and "master" in words:
    print("eligible for Bacheloer teching")
if "computer" in words and "bachleor" in words:
    print("eligible for 11 12 teaching")
 
#for HPE
if "Health & population" in words and "master" in words:
    print("eligible for Bacheloer teching")
if "Health & population" in words and "bachleor" in words:
    print("eligible for 11 12 teaching")

#for Account
if "Business Studies" in words and "master" in words:
    print("eligible for Bacheloer teching")
if "Health & population" in words and "bachleor" in words:
    print("eligible for 11 12 teaching")

else:
    print("not eligible")
