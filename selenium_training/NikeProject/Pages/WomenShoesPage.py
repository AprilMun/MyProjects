import self
import time

from selenium.webdriver.common.by import By

class womenShoesPage():
    def __init__(self, driver):
        self.driver = driver

    def First_women_shoe(self):

        women_page = self.driver.find_element(By.LINK_TEXT, "Women").click()
        women_shoes_page = self.driver.find_element(By.LINK_TEXT, "Shoes").click()
        women_shoe_results = self.driver.find_element(By.CLASS_NAME, "results__body")
        women_first_shoe = women_shoe_results.find_element(By.CLASS_NAME, "product-card")
        women_first_shoe_price = women_first_shoe.find_element(By.CLASS_NAME, "product-card__price")
        print(f"the price of first women shoe is {women_first_shoe_price.text}")
        return women_first_shoe_price.text