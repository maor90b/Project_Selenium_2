from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Firefox \
    (executable_path=r"C:\Users\Student\Desktop\Selenium\geckodriver.exe")

wait = WebDriverWait(driver, 10)

driver.implicitly_wait(10)

driver.get("https://juliemr.github.io/protractor-demo/")



driver.find_element_by_css_selector("input[ng-model='first']").send_keys("5")

select = Select(driver.find_element_by_xpath("//select[@ng-model='operator']"))

select.select_by_value("MULTIPLICATION")

driver.find_element_by_css_selector("input[ng-model='second']").send_keys("2" + Keys.ENTER)

text_result = driver.find_element_by_xpath("//h2[@class='ng-binding']").text

while text_result[0] == ".":

    text_result = driver.find_element_by_xpath("//h2[@class='ng-binding']").text


print(text_result,'is True')


















