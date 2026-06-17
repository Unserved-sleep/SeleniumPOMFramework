from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    txt_username = (By.ID,"user-name")
    txt_password = (By.ID,"password")
    btn_login = (By.ID,"login-button")

    def __init__(self,driver):
        self.driver = driver

    def set_username(self,username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                self.txt_username
            )
        ).send_keys(username)
    def set_password(self,password):
        self.driver.find_element(*self.txt_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.btn_login).click()