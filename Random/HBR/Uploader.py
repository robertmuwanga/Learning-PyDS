# Import relevant libraries
import os
import time
import pandas as pd
from selenium import webdriver

# Define required methods
def login(driver):
    # Navigate to login page
    login_page_url = 'https://hi-innovator.nssfug.org/authenticate/login'
    driver.get(login_page_url)

    # Define fields to submit information
    email_address_box = driver.find_element_by_name('email_address')
    password_box = driver.find_element_by_name('password')

    # Log into portal
    email_address = 'rmuwanga@nssfug.org'
    password = '@muw@ng@@N55FUG!'

    email_address_box.send_keys(email_address)
    password_box.send_keys(password)
    driver.find_element_by_tag_name('button').click()

if __name__ == '__main__':
    # Define default timeout (in secs)
    timeout = 5

    # Load pandas data frame with data
    data = pd.read_excel('HBR.xlsx', sheet_name='Final')

    # define webdriver
    driver = webdriver.Chrome()

    # Initial log in to admin panel.
    login(driver)
    time.sleep(5) # Allow page to load completely

    # Navigate to the podcast page
    driver.find_elements_by_link_text('view')[1].click()
    time.sleep(5)

    # Navigate to add podcasts page
    driver.find_element_by_tag_name('button').click()
    
    # Add podcasts
    for i in range(1) : # len(data):
        driver.find_element_by_xpath('//input[@formcontrolname="title"]').send_keys(data.loc[i, 'Subject'])
        driver.find_element_by_xpath('//textarea[@formcontrolname="description"]').send_keys(data.loc[i, 'description'])
        driver.find_element_by_xpath('//input[@type="file"]').send_keys(data.loc[i, 'Category'])
        driver.find_element_by_xpath('//input[@type="file"]').send_keys(os.path.join(os.getcwd(), data.loc[i, 'Filename']))

    # Cycle through pandas data frame to upload info
    # add column to data frame on successful and failed uploads
    # <-- TO DO -->

    # Logout of admin panel
    # <-- TO DO -->


    # Write data frame to file
    # <-- TO DO -->

    print('Upload process completed.')