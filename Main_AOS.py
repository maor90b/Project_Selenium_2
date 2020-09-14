from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage():
    def __init__(self, driver):
        self.driver = driver

    def FindCategory(self,category):
        self.driver.find_element_by_id(Categoties_id[category])

    def ClickCategory(self, category):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                            ((By.ID, Categoties_id[category] )))
        self.driver.find_element_by_id(Categoties_id[category]).click()


Categoties_id = {"Tablets": 'tabletsImg', "Laptops": 'laptopsImg', "Mice": 'miceImg', "Headphones": 'headphonesImg',
                     "Speakers": 'speakersImg'}




























