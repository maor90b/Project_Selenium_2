from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TabletsPage():
    def __init__(self, driver):
        self.driver = driver

    def  ClickProduct(self, ProductId):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, Products[ProductId])))
        self.driver.find_element_by_id(Products[ProductId]).click()


Products = {1 : '16', 2: '17', 3: '18'}



