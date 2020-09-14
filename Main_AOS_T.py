from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage():
    def __init__(self, driver):
        self.driver = driver

    # def TabletsPageClick(self):
    #     return self.driver.find_element_by_id("tabletsImg").click()
    #
    # def LaptopsPageClick(self):
    #     return self.driver.find_element_by_id("laptopsImg").click()
    #
    # def MicePageClick(self):
    #     return self.driver.find_element_by_id("miceImg").click()
    #
    # def HeadphonesPageClick(self):
    #     return self.driver.find_element_by_id("headphonesImg").click()
    #
    # def SpeakersPageClick(self):
    #     return self.driver.find_element_by_id("speakersImg").click()
    # #
    # def Cart(self):
    #     return self.driver.find_element_by_id("menuCart")
    #
    # def CartClick(self):
    #     return MainPage.Cart().click()
    #
    # def UserIconClick(self):
    #     return self.driver.find_element_by_id("menuUser").click()
    #
    # def UsernameSendKeys(self, username):
    #     return self.driver.find_element_by_name("username").send_keys(username)
    #
    # def PassWordSendKeys(self, password):
    #     return self.driver.find_element_by_name("password").send_keys(password)
    #
    # def SignInClick(self): # fixxxxx Keys
    #     # MainPage.UserClick()
    #     # MainPage.UsernameSendKeys()
    #     # MainPage.PassWordSendKeys()
    #     return self.driver.find_element_by_id("sign_in_btnundefined").click()

    def FindCategory(self,category):
        self.driver.find_element_by_id(Categoties_id[category])

    def ClickCategory(self, category):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                            ((By.ID, Categoties_id[category] )))
        self.driver.find_element_by_id(Categoties_id[category]).click()


Categoties_id = {"Tablets": 'tabletsImg', "Laptops": 'laptopsImg', "Mice": 'miceImg', "Headphones": 'headphonesImg',
                     "Speakers": 'speakersImg'}

