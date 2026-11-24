# AUTOMATING EMAILS WITH THE EZGMAIL MODULE

import ezgmail
ezgmail.init()

# Sending Mail
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email')  # replace templates with actual content
ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email',
['attachment1.jpg', 'attachment2.mp3']) # adding attachments to email

# NOTE: as part of its security and anti-spam features, Gmail might not send repeated emails with the exact same text (as these are likely spam) or emails that contain .exe or .zip file attachments (as they are potentially viruses).

ezgmail.send('recipient@example.com', 'Subject line', 'Body of the email', cc='friend@example.com', bcc='otherfriend@example.com, someoneelse@example.com') # optional keyword arguments cc and bcc to send carbon copies and blind carbon copies

# Check which Gmail address the token.json file is configured for
print(ezgmail.EMAIL_ADDRESS)


# Reading Email
# EZGmail has GmailThread and GmailMessage objects to represent conversation threads and individual emails, respectively. A GmailThread object has a messages attribute that holds a list of GmailMessage objects. The unread() function returns a list of GmailThread objects for the 25 most recent unread emails, which can then be passed to ezgmail.summary() to print a summary of the conversation threads in that list:
unread_threads = ezgmail.unread()  # List of GmailThread objects
ezgmail.summary(unread_threads)     # displays a quick summary of the gmail threads

# Accessing specific messages 
# The summary() function is handy for displaying a quick summary of the email threads, but to access specific messages (and parts of messages), you’ll want to examine the messages attribute of the GmailThread object. The messages attribute contains a list of the GmailMessage objects that make up the thread, and these have subject, body, timestamp, sender, and recipient attributes that describe the email:
len(unread_threads)                     # number of threads of unread mails
str(unread_threads[0])                  # the latest thread of unread mails
len(unread_threads[0].messages)         # get the length of unread mails in the latest thread of unread mails
str(unread_threads[0].messages[0])      # get the first mail from the latest unread thread
unread_threads[0].messages[0].subject   # get the subject of the first mail from the latest unread thread
unread_threads[0].messages[0].body      # get the body of the first mail from the latest unread thread
unread_threads[0].messages[0].timestamp # get the timestamp of the first mail from the latest unread thread
unread_threads[0].messages[0].sender    # get the sender of the first mail from the latest unread thread
unread_threads[0].messages[0].recipient # get the recipient of the first mail from the latest unread thread

# Retrieving more than the 25 most recent unread emails threads using maxResults argument
recent_threads = ezgmail.recent()
len(recent_threads)                     # max length here is 25
recent_threads = ezgmail.recent(maxResults=100)     # increase the max length to 100 threads
len(recent_threads)                     # max length here is 100


# Searching for Mail
result_threads = ezgmail.search('training')         # use ezgmail.search() to search for mails
len(result_threads)
ezgmail.summary(result_threads)

# NOTE: You can also pass to the search() function any of the special search operators that you can enter into the search box, such as the following:
"""
'label:UNREAD' For unread email

'from:al@inventwithpython.com' For email from al@inventwithpython.com

'subject:hello' For email with “hello” in the subject

'has:attachment' For email with file attachments

You can view a full list of search operators at https://support.google.com/mail/answer/7190.

"""


# Downloading Atachments
threads = ezgmail.search('vacation photos')             # get the thread of email with search result containing vacation photos
threads[0].messages[0].attachments              # get the attachment attribute of the latest message in the returned search result
threads[0].messages[0].downloadAttachment('tulips.jpg') # download the attachment tulips.jpg from the selected mail to the current working directory
threads[0].messages[0].downloadAllAttachments(downloadFolder='vacation2026')    # download all attachments in the selected mail to the folder vacation2026 in the cwd





