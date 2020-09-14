from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common import by
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox \
    (executable_path=r"C:\Users\Student\Desktop\Selenium\geckodriver.exe")

driver.get()