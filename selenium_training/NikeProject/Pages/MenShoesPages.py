import self
import time

from selenium.webdriver.common.by import By

class menShoesPage():
    def __init__(self, driver):
        self.driver = driver

    def First_men_shoe(self):

        men_page = self.driver.find_element(By.LINK_TEXT, "Men").click()
        men_shoes_page = self.driver.find_element(By.LINK_TEXT, "Shoes").click()
        men_shoe_results = self.driver.find_element(By.CLASS_NAME, "results__body")
        men_first_shoe = men_shoe_results.find_element(By.CLASS_NAME, "product-card")
        men_first_shoe_price = men_first_shoe.find_element(By.CLASS_NAME, "product-card__price")
        print(f"the price of first men shoe is {men_first_shoe_price.text}")
        return men_first_shoe_price.text