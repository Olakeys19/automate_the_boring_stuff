import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')
htmlElem = browser.find_element(By.TAG_NAME, 'html') # Find the <html> element of the page


buttons = [Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT]

try:
    while True:
        i = (random.randint(0, len(buttons)-1))
        htmlElem.send_keys(buttons[i])
except Exception as err:
    print('You closed the window')


