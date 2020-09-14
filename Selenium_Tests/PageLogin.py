from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageLogin():
    def __init__(self, driver):
        self.driver = driver

    def title(self):
        return self.driver.find_element_by_class_name("form-heading")

    def email(self):
        return self.driver.find_element_by_name("email")

    def emailSendKeys(self, user):
        self.email().send_keys(user)

    def password(self):
        return self.driver.find_element_by_name("password")

    def passSendKeys(self, pas):
        self.password().send_keys(pas)

    def loginKey(self):
        return self.driver.find_element_by_css_selector(".btn")

    def loginKeyClick(self):
        self.loginKey().click()

    def waitForLogin(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, ".dash>strong"))