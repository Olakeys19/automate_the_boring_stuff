# # OCR Fundamentals
# import pytesseract as tess
# from PIL import Image

# # Load an image
# img = Image.open("ocr-example.png")

# # Perform OCR
# text = tess.image_to_string(img)
# print(text)

# # NOTE:  Tesseract is intended for print documents rather than photos or handwritten text.


# import pytesseract as tess
# from PIL import Image
# img = Image.open('frankenstein.png')
# text = tess.image_to_string(img)
# print(text)


# # Recognizing Text in Non-English Languages
# import pytesseract as tess
# from PIL import Image
# img = Image.open('frankenstein_jpn.png')
# text = tess.image_to_string(img, lang='jpn')        # Specify the language for OCR
# print(text)

# # NOTE: To recognize text in multiple languages, you can combine language codes with a '+' character before passing it to the image_to_string() function’s lang keyword argument. For example, tess.image_to_string(img, lang='eng+jpn') recognizes both English and Japanese characters in an image.



# The NAPS2 Scanner Application
# Running NAPS2 from Python
import subprocess
naps2_path = [r'C:\Program Files\NAPS2\NAPS2.Console.exe']  # Windows
proc = subprocess.run(naps2_path + ['-i', 'frankenstein.png', '-o', 'output.pdf', '--install', 'ocr-eng', '--ocrlang', 'eng', '-n', '0', '-f', '-v'], capture_output=True)

"""
'-i', 'frankenstein.png' Sets the input as the frankenstein.png image file. See the next section, “Specifying Input,” for more information on specifying multiple inputs in various formats.

'-o', 'output.pdf' Creates a file named output.pdf to hold the OCR results.

'--install', 'ocr-eng' Installs the English language pack for OCR. This does nothing if the language is already installed. If you want to install a different language pack, use the ocr- prefix with another three-letter ISO 639 language code.

'--ocrlang', 'eng' Sets English as the language that the OCR scan recognizes. This argument is passed directly to Tesseract’s command line argument, so you could use an argument like 'eng+jpn+rus' to specify that the image has text in English, Japanese, and Russian.

'-n', '0' Specifies that you want to do zero scans and not use a flatbed scanner. This prevents error messages when there’s no physical flatbed scanner connected to your computer.

'-f' Forces NAPS2 to overwrite the output.pdf output file if a file with that name already exists.

'-v' Enables verbose mode so that status text appears as NAPS2 creates your PDF. If you want to see this status text, change the capture_output=True keyword argument for subprocess.run() to capture_output=False.
"""

# Specifying Input
# To specify multiple files, separate them with a semicolon. For example, passing '-i', 'cat.png;dog.png;moose.png' creates a PDF with cat.png used for the first page, dog.png used for the second page, and moose.png used for the third page.

# You can also specify individual pages in a PDF with syntax that is identical to Python’s list slice syntax. Follow the PDF filename with square brackets containing the page number to use. As in Python, 0 represents the first page. For example, passing '-i', 'spam.pdf[0];spam.pdf[5];eggs.pdf' creates a PDF with page 1 of spam.pdf, followed by page 6 of spam.pdf, and then all pages of eggs.pdf.

# You can specify a range of pages with this slice notation or use negative numbers to represent pages from the end of the PDF document. For example, passing '-i', 'spam.pdf[0:2];eggs.pdf[-1]' combines the first two pages of spam.pdf with the last page from eggs.pdf.