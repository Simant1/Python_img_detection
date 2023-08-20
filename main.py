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
    print("Congratulation you're eligible upto Bacheloer teching and your salary is upto 40000-50000 or negotiable")

if "math" in words and "bachelor" in words: 
    print("Congratulation you're eligible upto 11 12 teaching and your salary is 16000-17000")


#nepali
if "Nepali" in words and "bachleor" in words:
    print("Congratulation you're eligible upto 11 12 teaching and your salary is 16000-17000")
if "Nepali" in words and "master" in words:
    print("Congratulation you're eligible upto Bacheloer teching and your salary is upto 40000-50000 or negotiable")


#for social
if "social" in words and "master" in words:
    print("Congratulation you're eligible upto Bacheloer teching and your salary is upto 40000-50000 or negotiable")
if "social" in words and "bachleor" in words:
    print("Congratulation you're eligible upto 11 12 teaching and your salary is 16000-17000")

#for Science 
if "Science" in words and "master" in words:
    print("Congratulation you're eligible upto Bacheloer teching and your salary is upto 40000-50000 or negotiable")
if "Science" in words and "bachleor" in words:
    print("Congratulation you're eligible upto 11 12 teaching and your salary is 16000-17000")

#for computer
if "computer Science" in words and "master" in words:
    print("Congratulation you're eligible upto Bacheloer teching and your salary is upto 40000-50000 or negotiable")
if "computer Science" in words and "bachleor" in words:
    print("Congratulation you're eligible upto 11 12 teaching and your salary is 16000-17000")

#For Information technology Subject
if "Bachelor in Information Technology" in words and "master" in words:
    print("Congratulation you're eligible upto Bacheloer teching and your salary is upto 40000-50000 or negotiable")
if " master in Information Technology" in words and "bachleor" in words:
    print("Congratulation you're eligible upto 11 12 teaching and your salary is 16000-17000")
  
#for HPE
if "Health & population" in words and "master" in words:
    print("Congratulation you're eligible upto Bacheloer teching and your salary is upto 40000-50000 or negotiable")
if "Health & population" in words and "bachleor" in words:
    print(" Congratulation you're eligible upto 11 12 teaching and your salary is 16000-17000")

#for Account
if "Business Studies" in words and "master" in words:
    print("eligible upto Bacheloer teching and your salary is upto 40000-50000 or negotiable")
if "Health & population" in words and "bachleor" in words:
    print(" Congratulation you're eligible upto 11 12 teaching and your salary is 16000-17000")
else:
    print(" sorry ! you're not eligible")
