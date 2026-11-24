import pypdf
import pdfminer

# # NOTE: pypdf might not be able to extract texts from some PDFs, in such cases, pdfminer might be able to.
# pdfminer's extract_text() wors on entire PDFs

# # EXTRACTING TEXT
# PDF_FILENAME = 'Recursion_Chapter1.pdf'
# TEXT_FILENAME = 'recursion.txt'

# text = ''
# try:
#     reader = pypdf.PdfReader(PDF_FILENAME)
#     for page in reader.pages:
#       text += page.extract_text()
# except Exception:
#    text = pdfminer.high_level.extract_text(PDF_FILENAME)
# with open(TEXT_FILENAME, 'w', encoding='utf-8') as file_obj:
#    file_obj.write(text)

# EXTRACTING IMAGES

# # # Extracting text from pdf
# # pdfFileObj = open('meetingminutes.pdf', 'rb') # open minutes.pdf in read binary mode and save the file object
# # pdfReader = pypdf.PdfReader(pdfFileObj) # the PdfReader in pypdf is used to read the file object 
# # print(pdfReader.get_num_pages()) # get total number of pages in the pdf
# # pageObj = pdfReader.get_page(0)  # store the page object of page 0 in pageObj
# # print(pageObj.extract_text()) # get the text on page 0


# # # Decrypting Pages
# # pdfReader = pypdf.PdfReader(open('encrypted.pdf', 'rb')) # read the opened the pdf file object
# # print(pdfReader.is_encrypted) # check if it is 
# # # print(pdfReader.get_page(0)) # error because file is encrypted
# # pdfReader.decrypt('rosebud') # decrypt the pdf file object
# # pageObj = pdfReader.get_page(0)


# # Creating PDFs
# # # Copying Pages
# # pdf1File = open('meetingminutes.pdf', 'rb') # open as file object in read binary mode
# # pdf2File = open('meetingminutes2.pdf', 'rb')
# # pdf1Reader = pypdf.PdfReader(pdf1File) # read the contents
# # pdf2Reader = pypdf.PdfReader(pdf2File)
# # pdfWriter = pypdf.PdfWriter() # the class PdfWriter() is used for writing to pdf files

# # for pageNum in range(pdf1Reader.get_num_pages()):
# #     pageObj = pdf1Reader.get_page(pageNum)
# #     pdfWriter.add_page(pageObj)

# # for pageNum in range(pdf2Reader.get_num_pages()):
# #     pageObj = pdf2Reader.get_page(pageNum)
# #     pdfWriter.add_page(pageObj)

# # pdfOutputFile = open('combinedminutes.pdf', 'wb') # create output pdf file
# # pdfWriter.write(pdfOutputFile) # write the contents of pdfwriter to the pdf file
# # pdfOutputFile.close()
# # pdf1File.close()
# # pdf2File.close()

# # # Rotating Pages
# # minutesFile = open('meetingminutes.pdf', 'rb')
# # pdfReader = pypdf.PdfReader(minutesFile)
# # page = pdfReader.get_page(0)
# # page.rotate(90) # this function rotates a page clockwise by 90 degrees

# # pdfWriter = pypdf.PdfWriter()
# # pdfWriter.add_page(page)
# # resultPdfFile = open('rotatedPage.pdf', 'wb')
# # pdfWriter.write(resultPdfFile)
# # resultPdfFile.close()
# # minutesFile.close()

 
# # # Overlaying Pages
# # minutesFile = open('meetingminutes.pdf', 'rb')
# # pdfReader = pypdf.PdfReader(minutesFile)
# # minutesFirstPage = pdfReader.get_page(0)
# # pdfWatermarkReader = pypdf.PdfReader(open('watermark.pdf', 'rb'))
# # minutesFirstPage.merge_page(pdfWatermarkReader.get_page(0))
# # pdfWriter = pypdf.PdfWriter()
# # pdfWriter.add_page(minutesFirstPage)

# # for pageNum in range(1, pdfReader.get_num_pages()):
# #     pageObj = pdfReader.get_page(pageNum)
# #     pdfWriter.add_page(pageObj)

# # resultPdfFile = open('watermarkedCover.pdf', 'wb')
# # pdfWriter.write(resultPdfFile)
# # minutesFile.close()
# # resultPdfFile.close()


# # Encrypting PDFs
# pdfFile = open('meetingminutes.pdf', 'rb')
# pdfReader = pypdf.PdfReader(pdfFile)
# pdfWriter = pypdf.PdfWriter()
# for pageNum in range(pdfReader.get_num_pages()):
#     pdfWriter.add_page(pdfReader.get_page(pageNum))

# pdfWriter.encrypt('swordfish')
# resultPdf = open('encryptedminutes.pdf', 'wb')
# pdfWriter.write(resultPdf)
# resultPdf.close()




