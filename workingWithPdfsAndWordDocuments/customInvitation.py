#! python3
# customInvitation.py - generates a Word document with custom invitations

import docx

doc = docx.Document('style2.docx')                      # open style2.docx which has the designed custom styles: style1, style2, etc.

with open('guests.txt', 'r') as f_obj:                  # open guests.txt which has the names of guests to be invited
    guests = f_obj.read()                               # store the contents of guests.txt in the 'guests' variable
    guestList = guests.split('\n')                      # split the contents of guests by new line and save the returned list; this will make sure each guest name is an item in the list
    # print(guestList)
    for i, guest in enumerate(guestList, start=1):      # loop through the names in guest list, store the index as i starting from 1
        doc.add_paragraph('It would be a pleasure to have the comapny of', 'Style4')            # add first paragraph to the page and use custom Style4
        paraObj2 = doc.add_paragraph('', 'Style5')                                              # create second paragraph with an empty string and store the paragraph object as paraObj2
        doc.add_paragraph('at 11010 Memory Lane on the Evening of', 'Style4')   
        doc.add_paragraph('April 1st', 'Style6')
        paraObj5 = doc.add_paragraph("at 7 o'clock", 'Style4').add_run('')                      # add fifth paragraph and add a run of empty string so that page break can be added to this run.
        paraObj2.add_run(guest)                                                                 # Add the guest name from the list as the run for the second paragraph
        if i != len(guestList):                                                                 # check to make sure the guest name is not the last in the list so that page break will not be added at the end of the document
            doc.paragraphs[5*i].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)                 # add page break after every invitation except the last


doc.save('invitation.docx')





