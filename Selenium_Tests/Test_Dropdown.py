from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Firefox \
    (executable_path= r"C:\Users\Student\Desktop\Selenium\geckodriver.exe")

driver.implicitly_wait(10)

driver.get("http://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

driver.maximize_window()

select= Select(driver.find_element_by_id("select-demo"))
select.select_by_visible_text("Monday")

print(driver.find_element_by_class_name("selected-value"))



