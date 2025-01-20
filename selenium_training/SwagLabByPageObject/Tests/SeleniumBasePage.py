from selenium.webdriver.chrome.options import Options
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class seleniumBasePage():

    def selenium_start(self):
        print("start test")
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options = Options()

        options.add_argument('--no-sandbox')  # # Bypass OS security model
        options.add_argument('disable-infobars')
        options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(options=options)
        return driver

    def selenium_end(self,driver):
        print ("selenium end")
        driver.close()


# if it doesnt work, put this first:
#from selenium.webdriver.common.by import By
#from seleniumTraining.SeleniumBase import seleniumBase