# # # 1. webbrowser - comes with Python and opens a browser to a specific page
# # # 2. Requests - downloads files and web pages from the internet
# # # 3. BeautifulSoup - parses HTML and XML documents, making it easier to extract data from web pages
# # # 4. Selenium - automates web browsers, allowing you to interact with web pages and extract data dynamically


# # # import webbrowser

# # # # Open a specific URL in the default web browser
# # # webbrowser.open('http://inventwithpython.com/')


# # # Downloading Files from the Web with the requests Module
# # import requests

# # # res = requests.get('https://automatetheboringstuff.com/files/rj.txt') # Download the text file from the URL and store the response in the variable 'res'
# # # print(type(res)) # Print the type of the response object, which is <class 'requests.models.Response'>, indicating that 'res' is a Response object returned by the requests.get() function.
# # # print(res.status_code == requests.codes.ok) # Check if the status code of the response is equal to the 'OK' status code defined in the requests library. This will print 'True' if the request was successful (status code 200) and 'False' otherwise.
# # # print(len(res.text)) # Print the length of the text content of the response, which is the number of characters in the downloaded text file. This gives an indication of the size of the content that was downloaded.
# # # print(res.text[:250])


# # # Handling Download Errors with try and except
# # # res = requests.get('https://automatetheboringstuff.com/page_that_does_not_exist')
# # # # res.raise_for_status() # Check if the request was successful. If the status code indicates an error (e.g., 404 or 500), this will raise an HTTPError exception, which can be caught and handled in a try-except block.

# # # try:
# # #     res.raise_for_status() # Check if the request was successful. If the status code indicates an error (e.g., 404 or 500), this will raise an HTTPError exception, which can be caught and handled in a try-except block.
# # # except requests.exceptions.HTTPError as err:
# # #     print('There was a problem: %s' % (err)) # If an HTTPError exception is raised, this will print a message indicating that there was a problem, along with the error message provided by the exception. This allows you to handle errors gracefully and provide feedback to the user about what went wrong.


# # # # Saving Downloaded Files to the Hard Drive
# # # res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# # # res.raise_for_status() 
# # # playFile = open('RomeoAndJuliet.txt', 'wb') # Open a new file named 'RomeoAndJuliet.txt' in binary write mode ('wb') and assign the file object to the variable 'playFile'. This will create the file if it doesn't exist or overwrite it if it does.
# # # for chunk in res.iter_content(100000): # Iterate over the content of the response in chunks of 100,000 bytes using the iter_content() method of the response object. This allows you to download and save large files without consuming too much memory at once.
# # #     playFile.write(chunk) # Write each chunk of data to the file using the write() method of the file object. This will save the downloaded content to the hard drive in a memory-efficient way.
# # # playFile.close() # Close the file after writing to it to ensure that all data is properly saved and resources are released.


# # # Parsing HTML with the BeautifulSoup Module
# # import bs4
# # # res = requests.get('http://nostarch.com')
# # # res.raise_for_status()
# # # noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser') # Create a BeautifulSoup object named 'noStarchSoup' by parsing the text content of the response using the 'html.parser' parser. This allows you to navigate and search the HTML structure of the web page easily.
# # # print(type(noStarchSoup)) # Print the type of the noStarchSoup object, which is <class 'bs4.BeautifulSoup'>, indicating that it is a BeautifulSoup object created from the HTML content of the response.

# # # exampleFile = open('example.html')
# # # exampleSoup = bs4.BeautifulSoup(exampleFile, 'html.parser')
# # # print(type(exampleSoup))


# # # # Examples of CSS Selectors
# # # # 1. soup.select('div') - Selects all <div> elements in the HTML document.
# # # # 2. soup.select('#author') - Selects the element with the id attribute equal to 'author'.
# # # # 3. soup.select('.notice') - Selects all elements with the class attribute equal to 'notice'.
# # # # 4. soup.select('div span') - Selects all <span> elements that are descendants of <div> elements.
# # # # 5. soup.select('div > span') - Selects all <span> elements that are direct children of <div> elements.
# # # # 6. soup.select('input[name]') - Selects all <input> elements that have a name attribute, regardless of its value.
# # # # 7. soup.select('input[type="button"]') - Selects all <input> elements that have a type attribute equal to 'button'.

# # # exampleFile = open('example.html')
# # # exampleSoup = bs4.BeautifulSoup(exampleFile.read(), 'html.parser')
# # # elems = exampleSoup.select('#author') # Use the select() method of the BeautifulSoup object to find all elements with the id attribute equal to 'author' and store the result in the variable 'elems'. This will return a list of matching elements.
# # # print(type(elems))
# # # print(len(elems))
# # # print(type(elems[0]))
# # # print(elems[0].getText())
# # # print(str(elems[0]))
# # # print(elems[0].attrs)

# # # pElems = exampleSoup.select('p')
# # # print(str(pElems[0]))
# # # print(len(pElems))
# # # print(pElems[0].getText())


# # # # Getting Data from an ELement’s Attributes
# # # soup = bs4.BeautifulSoup(open('example.html'), 'html.parser')
# # # spanElem = soup.select('span')[0] # Select the first <span> element from the HTML document and store it in the variable 'spanElem'.
# # # print(spanElem)
# # # print(spanElem.get('id')) # Get the value of the 'id' attribute of the selected <span> element using the get() method and print it. This will return the value of the 'id' attribute if it exists, or None if it does not.
# # # print(spanElem.get('some_nonexistent_addr') == None) 
# # # print(spanElem.attrs) # Print the attributes of the selected <span> element as a dictionary using the attrs property. This will show all the attributes and their corresponding values for that element.


# # # Controlling the Browser with the Selenium Module
# # from selenium import webdriver
# # browser = webdriver.Firefox() # Create a new instance of the Firefox web browser using Selenium's webdriver. This will open a new Firefox window that can be controlled programmatically.
# # # print(type(browser)) # Print the type of the 'browser' object, which is <class 'selenium.webdriver.firefox.webdriver.WebDriver'>, indicating that it is a WebDriver object specific to the Firefox browser.
# # browser.get('http://inventwithpython.com') 

# # # Selenium's WebDriver's Methods for Finding Elements on a Web Page
# # # 1. find_element(s)(By.ID, id) - Finds an element by its unique id attribute.
# # # 2. find_element(s)(By.NAME, name) - Finds an element by its name attribute.
# # # 3. find_element(s)(By.CLASS_NAME, class_name) - Finds an element by its class attribute.
# # # 4. find_element(s)(By.CSS_SELECTOR, css_selector) - Finds an element using a CSS selector.
# # # 5. find_element(s)(By.LINK_TEXT, link_text) - Finds a link element by its visible text.
# # # 6. find_element(s)(By.PARTIAL_LINK_TEXT, partial_link_text) - Finds a link element by a partial match of its visible text.
# # # 7. find_element(s)(By.TAG_NAME, tag_name) - Finds an element by its tag name.

# # # WebElement Attributes and Methods
# # # 1. tag_name - The tag name of the element (e.g., 'div', 'a', 'span').
# # # 2. get_attribute(name) - Returns the value for the element's name attribute
# # # 3. text - The text within the element, such as 'hello' for <span>hello</span>.
# # # 4. clear() - Clears the text if it's a text entry element.
# # # 5. is_displayed() - Returns True if the element is visible on the page, False otherwise.
# # # 6. is_enabled() - Returns True if the element is enabled (i.e., can be interacted with), False otherwise.
# # # 7. is_selected() - Returns True if the element is selected (e.g., for checkboxes or radio buttons), False otherwise.
# # # 8. location - A dictionary with the x and y coordinates of the element on the page.

# # Example usage
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()    

# # 1.
# # browser.get('http://inventwithpython.com')
# # try:
# #     elem = browser.find_element(By.CLASS_NAME, 'img-thumb')
# #     print('Found <%s> element with that class name!' % (elem.tag_name))
# # except:
# #     print('Was not able to find an element with that name.')

# # # 2. Clicking an Element
# # browser.get('http://inventwithpython.com')
# # linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
# # print(type(linkElem))
# # linkElem.click() # Click the link to navigate to the next page

# # # 3. Filling out and Submitting Forms
# # browser.get('https://www.freelancer.com/login') # Navigate to the Freelancer login page
# # emailElem = browser.find_element(By.ID, 'emailOrUsernameInput') # Find the email input field by its ID
# # emailElem.send_keys('your_email_address') # enter 'your_email_address' into the email input field
# # passwordElem = browser.find_element(By.ID, 'passwordInput') # Find the password input field by its ID 
# # passwordElem.send_keys('12345') # enter '12345' into the password input field
# # passwordElem.submit() # Submit the form, which will attempt to log in with the provided credentials

# # Commonly used variables in the selnium.webdriver.common.keys module
# # from selenium.webdriver.common.keys import Keys
# # 1. Keys.ENTER, Keys.RETURN - Represents the Enter and Return keys on the keyboard.
# # 2. Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT - Represents the arrow keys for navigating through elements or text.
# # 3. Keys.HOME, Keys.END, Keys.PAGE_UP, Keys.PAGE_DOWN - Represents the Home, End, Page Up, and Page Down keys for scrolling or navigating through content.
# # 4. Keys.BACKSPACE, Keys.DELETE, Keys.ESCAPE - Represents the Backspace, Delete, and Escape keys
# # 5. Keys.TAB, Keys.SHIFT, Keys.CONTROL, Keys.ALT - Represents the Tab, Shift, Control, and Alt keys for keyboard shortcuts and navigation.
# # 6. Keys.F1, Keys.F2, ..., Keys.F12 - Represents the function keys on the keyboard for various actions and shortcuts.

# # Example usage
# # from selenium.webdriver.common.keys import Keys
# # browser.get('http://nostarch.com')
# # htmlElem = browser.find_element(By.TAG_NAME, 'html') # Find the <html> element of the page
# # htmlElem.send_keys(Keys.END) # Scroll to the bottom of the page by sending the END key to the <html> element
# # htmlElem.send_keys(Keys.HOME) # Scroll back to the top of the page by sending the HOME key to the <html> element

# # Clicking Browser Buttons
# # 1. browser.back() - Simulates clicking the Back button in the browser, navigating to the previous page in the browsing history.
# # 2. browser.forward() - Simulates clicking the Forward button in the browser, navigating to the next page in the browsing history if available.
# # 3. browser.refresh() - Simulates clicking the Refresh button in the browser, reloading the current page.
# # 4. browser.quit() - Closes the browser window and ends the WebDriver session.

# input("Press Enter to close...")
# browser.quit()

