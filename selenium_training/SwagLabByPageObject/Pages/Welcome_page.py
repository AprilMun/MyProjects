from selenium.webdriver.common.by import By


class welcomePage():

    def __init__(self,driver):
        self.driver = driver

    def get_first_price (self):
        print("getting the first product price")
        first_price = self.driver.find_element(By.CLASS_NAME, "inventory_item_price")
        price = first_price.text
        print(f"the first price is {price}")