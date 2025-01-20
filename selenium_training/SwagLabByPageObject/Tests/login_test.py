from selenium_training.SwagLabByPageObject.Pages.Login_page import loginPage
from selenium_training.SwagLabByPageObject.Pages.Welcome_page import welcomePage
from selenium_training.SwagLabByPageObject.Tests.SeleniumBasePage import seleniumBasePage

class loginTest():
    base = seleniumBasePage()
    driver = base.selenium_start()
    login_page = loginPage(driver)
    welcome_page = welcomePage(driver)

    driver.get("https://www.saucedemo.com/")

    login_page.print_details()
    login_page.login_by_user_password("standard_user","secret_sauce")
    welcome_page.get_first_price()

    base.selenium_end(driver)