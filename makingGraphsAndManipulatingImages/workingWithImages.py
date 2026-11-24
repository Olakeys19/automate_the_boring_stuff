# Colors and RGBA values
# A is alpha which represents transparency

# Using Pillow module

# from PIL import ImageColor
# ImageColor.getcolor('red', 'RGBA')      # color name string is case-insensitive 
# ImageColor.getcolor('Red', 'RGBA')      # get the RGBA value for red
# ImageColor.getcolor('RED', 'RGBA')
# ImageColor.getcolor('black', 'RGBA')
# ImageColor.getcolor('red', 'RGBA')
# ImageColor.getcolor('red', 'RGBA')
# ImageColor.getcolor('cornflowerBlue', 'RGBA')

# list(ImageColor.colormap)   # view all the color names

# # Coordinates and Box Tuples
# """
# Many of Pillow’s functions and methods take a box tuple argument. This means Pillow is expecting a tuple of four integer coordinates that represent a rectangular region in an image. The four integers are, in order, as follows:

# Left The x-coordinate of the leftmost edge of the box.

# Top The y-coordinate of the top edge of the box.

# Right The x-coordinate of one pixel to the right of the rightmost edge of the box. This integer must be greater than the left integer.

# Bottom The y-coordinate of one pixel lower than the bottom edge of the box. This integer must be greater than the top integer.
# """

# # Manipulating Images with Pillow
# from PIL import Image
# cat_im = Image.open('zophie.png')       # open the image and store in cat_im as an image object
# cat_im.show()           # display the image

# # Working with the Image Data Type
# cat_im.size     #   get the image dimensions (width, size)
# width, height = cat_im.size
# cat_im.filename     # get the filename of the image object
# cat_im.format       # get the image format
# cat_im.format_description   # describe the format
# cat_im.save('zophie.jpg')   # save image object as a new image, zophie.jpg (we changed the extension)


# # Creating Images
# from PIL import Image
# im = Image.new('RGBA', (100, 200), 'purple')        # create a new image object in RGBA mode with width and height of 100 and 200 respectively, purple background
# im.save('purpleImage.png')  # create a new image object in RGBA mode with width and height of 20, no color means transparent
# im2 = Image.new('RGBA', (20, 20))
# im2.save('transparentImage.png')


# # Cropping Images
# cat_im = Image.open('zophie.png')
# cropped_im = cat_im.crop((335, 345, 565, 560))
# cropped_im.save('cropped.png')

# # Pasting Images onto Other Images
# from PIL import Image
# cat_im = Image.open('zophie.png')       
# cat_copy_im = cat_im.copy()     # copy the image object in cat_im to cat_copy_im

# face_im = cat_im.crop((335, 345, 565, 560)) # crop the image and save the cropped in face_im

# face_im.size
# cat_copy_im.paste(face_im, (0, 0))  # paste the cropped image at coordinates (0, 0) of cat_copy_im
# cat_copy_im.paste(face_im, (400, 500))      # paste the cropped image at coordinates (400, 500) of cat_copy_im
# cat_copy_im.save('pasted.png')      # save cat_copy_im as pasted.png

# # Tiled Image 
# cat_im_width, cat_im_height = cat_im.size
# face_im_width, face_im_height = face_im.size
# cat_copy_im = cat_im.copy()
# for left in range(0, cat_im_width, face_im_width):  # loop over the width of the image starting from 0, increment using width of the pasted image 
#     for top in range(0, cat_im_height, face_im_height): # loop over the height of the image starting from 0, increment using height of the pasted image 
#         print(left, top)
#         cat_copy_im.paste(face_im, (left, top)) # paste image at the left and top coordinates of each iteration
# cat_copy_im.save('tiled.png')

# # Resizing Images
# cat_im = Image.open('zophie.png')
# width, height = cat_im.size
# quarter_sized_im = cat_im.resize((int(width / 2), int(height / 2))) # resize image to half width and half height
# quarter_sized_im.save('quartersized.png')
# svelte_im = cat_im.resize((width, height + 300))    # resize image to height plus 300
# svelte_im.save('svelte.png')


# # Rotating and Flipping Images
# from PIL import Image
# cat_im = Image.open('zophie.png')
# cat_im.rotate(90).save('rotated90.png')     # rotate image counterclockwise by 90 degrees and save rotated image
# cat_im.rotate(-90).save('rotated-90.png')     # rotate image clockwise by 90 degrees and save rotated image
# cat_im.rotate(180).save('rotated180.png')
# cat_im.rotate(270).save('rotated270.png')

# cat_im.rotate(6).save('rotated6.png')
# cat_im.rotate(6, expand=True).save('rotated6_expanded.png') # optional expand keyword argument set to True to enlarge the dimensions of the image to fit the entire rotated new image

# cat_im.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')     # mirror-flipping with the transpose() method
# cat_im.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

 
# # Changing Individual Pixels
# from PIL import Image
# im = Image.new('RGBA', (100, 100))  # make a new image that is a 100×100 transparent square
# im.getpixel((0, 0))  # Calling getpixel() on coordinates in this image returns (0, 0, 0, 0) because the image is transparent 

# # Color the top half of the image light gray
# for x in range(100):        # loop over the full width of the image
#     for y in range(50):     # loop over half the height of the image
#         im.putpixel((x, y), (210, 210, 210))    # set each pixel to light gray

# # # Color the bottom half of the image dark gray
# from PIL import ImageColor
# for x in range(100):            # loop over the full width of the image
#     for y in range(50, 100):    # loop over bottom half of the image
#         im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))    # # set each pixel to light gray. The putpixel() method doesn’t accept a standard color name like 'darkgray', so we use ImageColor.getcolor() to get a corresponding color tuple

# print(im.getpixel((0, 0)))
# print(im.getpixel((0, 50)))
# im.save('putPixel.png')



# # DRAWING ON IMAGES
# # Using Pillow’s ImageDraw module

# from PIL import Image, ImageDraw
# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)

# """
# Shapes
# The following ImageDraw methods draw various kinds of shapes on the image. The fill and outline parameters for these methods are optional and will default to white if left unspecified.

# Points
# The point(xy, fill) method draws individual pixels. The xy argument represents a list of the points to draw. The list can contain x- and y-coordinate tuples, such as [(x, y), (x, y), ...], or x- and y-coordinates without tuples, such as [x1, y1, x2, y2, ...]. The fill argument colors the points and can be either an RGBA tuple or a string, such as 'red'. The fill argument is optional. The “point” name here refers to a pixel, not the unit of font size.

# Lines
# The line(xy, fill, width) method draws a line or series of lines. The xy argument is either a list of tuples, such as [(x, y), (x, y), ...], or a list of integers, such as [x1, y1, x2, y2, ...]. Each point is a connecting points on the lines you’re drawing. The optional fill argument specifies the color of the lines as an RGBA tuple or color name. The optional width argument determines the width of the lines, and defaults to 1 if left unspecified.

# Rectangles
# The rectangle(xy, fill, outline, width) method draws a rectangle. The xy argument is a box tuple of the form (left, top, right, bottom). The left and top values specify the x- and y-coordinates of the upper-left corner of the rectangle, while right and bottom specify the coordinates of the lower-right corner. The optional fill argument is the color of the inside of the rectangle. The optional outline argument is the color of the rectangle’s outline. The optional width argument represents the width of the lines, and defaults to 1 if left unspecified.

# Ellipses
# The ellipse(xy, fill, outline, width) method draws an ellipse. If the width and height of the ellipse are identical, this method will draw a circle. The xy argument is a box tuple (left, top, right, bottom) representing a box that precisely contains the ellipse. The optional fill argument is the color of the inside of the ellipse, and the optional outline argument is the color of the ellipse’s outline. The optional width argument is the width of the lines, and defaults to 1 if left unspecified.

# Polygons
# The polygon(xy, fill, outline, width) method draws an arbitrary polygon. The xy argument is a list of tuples, such as [(x, y), (x, y), ...], or integers, such as [x1, y1, x2, y2, ...], representing the connecting points of the polygon’s sides. The last pair of coordinates will automatically connect to the first pair. The optional fill argument is the color of the inside of the polygon, and the optional outline argument is the color of the polygon’s outline. The optional width argument is the width of the lines, and defaults to 1 if left unspecified.
# """

# # Drawing Example
# from PIL import Image, ImageDraw
# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black') 
# draw.rectangle((20, 30, 60, 60), fill='blue')
# draw.ellipse((120, 30, 160, 60), fill='red')
# draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')
# for i in range(100, 200, 10):
#     draw.line([(i, 0), (200, i - 100)], fill='green')

# im.save('drawing.png')


# # TEXT
# """
# The ImageDraw object also has a text() method for drawing text onto an image. This method takes four arguments:

# xy A two-integer tuple specifying the upper-left corner of the text box

# text The string of text you want to write

# fill The color of the text

# font An optional ImageFont object used to set the typeface and size of the text
# """

# from PIL import Image, ImageDraw, ImageFont
# import os
# im = Image.new('RGBA', (200, 200), 'white')
# draw = ImageDraw.Draw(im)
# draw.text((20, 150), 'Hello', fill='purple')
# arial_font = ImageFont.truetype('arial.ttf', 32)
# draw.text((100, 150), 'Howdy', fill='gray', font=arial_font)
# im.save('text.png')


# COPYING AND PASTING IMAGES TO THE CLIPBOARD USING PYPERCLIPIMG MODULE
# The pyperclipimg.copy() function takes a Pillow Image object and puts it on your operating system’s clipboard. You can then paste it into a graphics or image processing program such as MS Paint
from PIL import Image
im = Image.open('zophie.png')

import pyperclipimg
pyperclipimg.copy(im)
pasted_im = pyperclipimg.paste() # Now copy a new image to the clipboard.

# Paste the clipboard contents to a graphics program.
pasted_im.show()  # Shows the image from the clipboard
