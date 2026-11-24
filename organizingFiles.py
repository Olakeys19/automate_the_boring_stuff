# Copying files and folders
# The shutil module has a number of functions for copying files and folders. The shutil.copy() function copies a single file, while the shutil.copytree() function copies an entire folder and every folder and file contained in it.

import os, shutil, zipfile

# # Copying files
# # shutil.copy(source, destination)
# # shutil.copytree(source, destination)
# shutil.copy('hello.txt', 'hello2.txt') # copies the contents of hello.txt to a new file called hello2.txt. If hello2.txt already exists, it will be overwritten.
# # N.B If a directory is not specified, the file will be copied from and to the current working directory.
# shutil.copy('spam.txt', '.\\delicious') # copies the contents of spam.txt to the delicious folder. The new file will have the same name as the original file (spam.txt).

# # shutil.copytree() function copies an entire folder and every folder and file contained in it. The destination directory must not already exist.
# shutil.copytree('.\\delicious', '.\\delicious_backup') # copies the delicious folder and all its contents to a new folder called delicious_backup. If delicious_backup already exists, an error will be raised.

# # Moving and renaming files and folders
# # shutil.move(source, destination)
# shutil.move('hello2.txt', '.\\delicious') # moves the hello2.txt file to the delicious folder. If a file with the same name already exists in the destination folder, it will be overwritten.
# shutil.move('hello.txt', '.\\delicious\\hello3.txt') # moves the hello.txt file to the delicious folder and renames it to hello3.txt. If a file with the same name already exists in the destination folder, it will be overwritten.
# shutil.move('.\\delicious', '.\\delicious_backup') # moves the delicious folder and all its contents to the delicious_backup folder. If the delicious_backup folder already exists, it will be overwritten.

# # N.B: if destination folder does not exist, the file being copied will be renamed as the specified destination name.


# # Permanently deleting files and folders
# # Calling os.unlink(path) will permanently delete the file at the specified path. 
# # Calling os.rmdir(path) will permanently delete the folder at the specified path, but only if the folder is empty. If the folder contains any files or folders, an error will be raised.
# # Calling shutil.rmtree(path) will permanently delete the folder at the specified path, along with all the files and folders contained in it.


# # Safe deletes with the send2trash module
# # The send2trash module sends files and folders to the recycle bin instead of permanently deleting them

# import send2trash
# send2trash.send2trash('.\\delicious_backup') # sends the delicious_backup folder and all its contents to the recycle bin. The folder can be restored from the recycle bin if needed.    

# # Walking a Directory Tree
# # os.walk()  
# for folderName, subfolders, filenames in os.walk('.\\delicious'):
#     print(f'The current folder is {folderName}')

#     for subfolder in subfolders:
#         print(f'SUBFOLDER OF {folderName}: {subfolder}')

#     for filename in filenames:
#         print(f'FILE INSIDE {folderName}: {filename}')
    
#     print('')


# COMPRESSING FILES WITH THE ZIPFILE MODULE

# # Reading ZIP files
# exampleZip = zipfile.ZipFile('delicious.zip')
# print(exampleZip.namelist()) # returns a list of strings for each file and folder in the zip file. Folders are identified by a trailing slash (/) at the end of the string.

# helloInfo = exampleZip.getinfo('delicious/hello.txt') # returns a ZipInfo object about the specified file in the zip file. The ZipInfo object has a file_size attribute that gives the size of the uncompressed file, and a compress_size attribute that gives the size of the compressed file.
# print(f'{helloInfo.file_size} bytes')
# print(f'{helloInfo.compress_size} bytes')
# print (f'Compressed file is {round(helloInfo.file_size / helloInfo.compress_size, 2)} times smaller!')
# exampleZip.close()

# Extracting from ZIP Files
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall() # extracts all the files and folders from the zip file into the current working directory. If there are any folders in the zip file, they will be created in the current working directory. If there are any files in the zip file that have the same name as an existing file in the current working directory, they will be overwritten

exampleZip.extract('delicious/hello.txt', '.\\extracted') # extracts the delicious/hello.txt file from the zip file into the extracted folder. If the extracted folder does not already exist, it will be created.
exampleZip.close()

# Creating and Adding to ZIP Files
newZip = zipfile.ZipFile('new.zip', 'w') # creates a new zip file called new.zip.
# the 'w' argument works like in open() function, use 'a' to append to an existing zip file instead of overwriting it.
newZip.write('delicious/hello.txt', compress_type=zipfile.ZIP_DEFLATED) # adds the delicious/hello.txt file to the new.zip file. The compress_type argument specifies that the file should be compressed using the ZIP_DEFLATED compression method.
newZip.close()