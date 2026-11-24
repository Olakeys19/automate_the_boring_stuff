import docx

# # The python-docx module helps python to create and modify word documents
# # A Run object is a contiguous run of text with the same style
# # A new Run object is needed whenever the style changes

# # # Reading Word Documents
# # doc = docx.Document('demo.docx') # open a document object from the file demo.docx
# # print(len(doc.paragraphs)) # print the number of paragraphs in the document

# # print(doc.paragraphs[0].text) # print the first paragraph's text
# # print(doc.paragraphs[6].text)
# # print(len(doc.paragraphs[1].runs)) # print the number of runs in the second paragraph of the word document
# # print(doc.paragraphs[1].runs[0].text) # print the text of the first run in the second paragraph
# # print(doc.paragraphs[1].runs[1].text)
# # print(doc.paragraphs[1].runs[2].text)
# # print(doc.paragraphs[1].runs[3].text)


# # # Getting only the full text from a .docx file
# # def get_text(filename):
# #     doc = docx.Document(filename)
# #     full_text = []
# #     for para in doc.paragraphs:
# #         full_text.append(para.text)
# #     return '\n'.join(full_text)

# # print(get_text('demo.docx'))


# # Styling Paragraphs and Run Objects
# # Word documents contain three types of styles:
# # 1. Paragraph styles - apply to paragraph objects
# # 2. Character styles - apply to Run objects
# # 3. Linked styles - apply to both kinds of objects
# """
# Default word styles: 
# 'Normal'   'Heading 5' 'List Bullet'       'List Paragraph'
# 'Body Text' 'Heading 6' 'List Bullet 2'     'MacroText'
# 'Body Text 2'   'Heading 7' 'List Bullet 3'     'No Spacing'
# 'Body Text 3'   'Heading 8' 'List Continue'     'Quote'
# 'Caption'   'Heading 9' 'List Continue 2'   'Subtitle'
# 'Heading 1' 'Intense Quote' 'List Continue 3'   'TOC Heading'
# 'Heading 2' 'List'      'List Number '      'Title'
# 'Heading 3' 'List 2'    'List Number 2' 
# 'Heading 4' 'List 3'    'List Number 3' 
# """
# # When using a linked style for a run object, add 'Char' to the end of its name
# # E.g: paragraphObj.style = 'Quote' but runObj.style = 'Quote char'
# # NOTE: To create custom styles, use the Word application to define them, then read them from the style attribute of a Paragraph or Run object.

# # Applying Run Attributes
# """
# bold                        The text appears in bold.
# italic                      The text appears in italic.
# underline                   The text is underlined.
# strike                      The text appears with strikethrough.
# double_strike               The text appears with double strikethrough.
# all_caps                    The text appears in capital letters.
# small_caps                  The text appears in capital letters, with lowercase letters two points smaller.
# shadow                      The text appears with a shadow.
# outline                     The text appears outlined rather than solid.
# rtl                         The text is written right-to-left.
# imprint                     The text appears pressed into the page.
# emboss                      The text appears raised off the page in relief
# """

# # Example
# doc = docx.Document('demo.docx')
# print(doc.paragraphs[0].text)
# print(doc.paragraphs[0].style) # print the style of the first paragraph
# doc.paragraphs[0].style = 'Normal' # set the style to normal
# print((doc.paragraphs[1].runs[0].text, doc.paragraphs[1].runs[1].text, doc.paragraphs[1].runs[2].text, doc.paragraphs[1].runs[3].text))
# doc.paragraphs[1].runs[0].style = 'Quote Char' # set run style to quote
# doc.paragraphs[1].runs[1].underline = True # underline run
# doc.paragraphs[1].runs[3].underline = True
# doc.save('restyled.docx')

# WRITING WORD DOCUMENTS
# # Creating word documents
# doc = docx.Document() # create a new document object 
# doc.add_paragraph('Hello, world!', 'Title') # adds a new paragraph and style with title styling
# doc.save('helloworld.docx') # save the document object to the file helloworld.docx

# # Adding paragraph and runs
# para_0bj_1 = doc.add_paragraph('This is a second paragraph.') # add a paragraph and save the paragraph object for future use
# para_0bj_2 = doc.add_paragraph('This is yet another paragraph.')
# para_0bj_1.add_run(' This text is being added to the second paragraph.') # add a run to the paragraph 1 object
# doc.save('multipleParagraphs.docx')

# # Adding Headings
# # calling add_heading() adds a paragraph with one of the heading styles
# doc = docx.Document()
# doc.add_heading('Header 0', 0) # add text 'Header 0' and set heading level to 0
# doc.add_heading('Header 1', 1)
# doc.add_heading('Header 2', 2)
# doc.add_heading('Header 3', 3)
# doc.add_heading('Header 4', 4)
# doc.save('headings.docx')

# # Adding Line and Page Breaks
# To add a line break (rather than starting a whole new paragraph), you can call the add_break() method on the Run object you want to have the break appear after. If you want to add a page break instead, you need to pass the value docx.enum.text.WD_BREAK.PAGE as a lone argument to add_break()
# doc = docx.Document()
# doc.add_paragraph('This is on the first page!')
# doc.paragraphs[0].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE) # adding page break
# doc.add_paragraph('This is on the second page!').add_run('Run 1 has been added')
# doc.paragraphs[1].runs[0].add_break() # adding line break
# doc.save('twoPage.docx')

# Adding Pictures
# You can use the add_picture() method of Document objects to add an image to the end of the document. Say you have a file zophie.png in the current working directory. You can add zophie.png to the end of your document with a width of 1 inch and height of 4 centimeters (Word can use both imperial and metric units) by entering the following:
doc = docx.Document()
doc.add_picture('zophie.png', width=docx.shared.Inches(1), height=docx.shared.Cm(4))
doc.save('picture.docx')














