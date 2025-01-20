from selenium.webdriver.common.by import By


class loginPage():

    def __init__(self,driver):
        self.driver = driver

    def print_details(self):
        print("Hi")

    #standard_user
    # secret_sauce
    def login_by_user_password(self,user_text,password_text):
        user = self.driver.find_element(By.ID, "user-name")

        user.click()
        user.send_keys(user_text)

        password = self.driver.find_element(By.ID, "password")
        password.click()
        password.send_keys(password_text)

        self.driver.find_element(By.ID, "login-button").click()

