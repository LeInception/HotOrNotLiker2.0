from selenium import webdriver
import time
import random

MAX_WAIT_BETWEEN_LIKES = 5000 # in milliseconds
LIKE_PERCENTAGE = 90 # percentage that should be swiped right

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://chatdate.app/signin/')

logged_in = False

while not logged_in:
    current_url = driver.current_url
    if(not '.chatdate.app/encounters' in current_url):
        time.sleep(1)
        print("Waiting till user has logged in....")
        print("  Current URL: "  + current_url)
    else:
        print(current_url)
        print("\nSuccesfully logged in")
        logged_in = True

time.sleep(3)
        

while True:
    try:
        yes_button = driver.find_element_by_xpath('//div[@data-choice="yes"]')
        no_button = driver.find_element_by_xpath('//div[@data-choice="no"]')
        wait_delay = random.randrange(0, MAX_WAIT_BETWEEN_LIKES)/1000
        time.sleep(wait_delay)
        if(random.randrange(0, 100) < LIKE_PERCENTAGE):
            yes_button.click()
        else:
            no_button.click()
    except:
        print("Error, continuing...")
