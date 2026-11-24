#! python3
# encryptPdfs.py - encrypts all PDFs in a folder and all its subfolders

import os, pypdf

os.chdir(r'C:\Users\ogoay\OneDrive\Desktop\python_work\workingWithPdfsAndWordDocuments\New folder') # change the directory to the folder you want to encrypt PDFs

for folder, subfolder, filenames in os.walk(os.curdir): # loop through all subfolders and files in the current directory
    for filename in filenames:                          # loop through all the files
        if filename.endswith('.pdf'):                   # select only pdf files
            directory = os.path.abspath(folder + os.path.sep + filename)        # store the absolute path of the filename in the variable directory
            # print(directory)
            pdfFile  = open(directory, 'rb')                                    # open a pdf file object of the current file
            reader = pypdf.PdfReader(pdfFile)                                   # create a reader object of the file
            writer = pypdf.PdfWriter()                                          # create a pdf writer object
            for pageNum in range(reader.get_num_pages()):                       # loop through all the pages in the pdf file
                writer.add_page(reader.get_page(pageNum))                       # add each page to the pdf writer object
            writer.encrypt('password')                                          # add an encryption to the writer object
            resultPdf = open(f'{folder}{os.path.sep}{filename.split('.pdf')[0]}_encrypted.pdf', 'wb')   # create an output pdf file to store the contents of pdf writer
            writer.write(resultPdf)                                             # write the contents of the pdf writer to the new pdf file
            resultPdf.close()                                                   # close the output pdf file
            pdfFile.close()                                                     # close the pdf file object

print('Done')