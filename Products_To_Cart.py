from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Product_Purchase():
    def __init__(self, driver):
        self.driver = driver

    def Quantity(self, quantity):
        self.driver.find_element_by_css_selector("input[numbers-only='""']").click()
        self.driver.find_element_by_css_selector("input[numbers-only='""']").send_keys(quantity)

    def Click_Add_To_Cart(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.CSS_SELECTOR, "button[translate='ADD_TO_CART']")))
        self.driver.find_element_by_css_selector("button[translate='ADD_TO_CART']").click()







