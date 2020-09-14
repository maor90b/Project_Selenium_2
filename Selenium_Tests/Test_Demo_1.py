from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox \
    (executable_path=r"C:\Users\Student\Desktop\Selenium\geckodriver.exe")

driver.implicitly_wait(10)  # wait a few seconds before each action

driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")

# driver.maximize_window()

try:
    driver.find_element_by_css_selector("a#at-cv-lightbox-close").click()
except NoSuchElementException:
    pass

driver.find_element_by_id("user-message").send_keys("my message")

# driver.find_element_by_Xpath("//input[@id='user-message']").send_keys("my message")
# driver.find_element_by_css_selector("input[id='user-message'][placeholder='Please enter your Message']")
# driver.find_element_by_css_selector("input#'user-message')
# driver.find_element_by_css_selector("button[class='btn btn-default'][onclick='showInput();']").click()
driver.find_element_by_xpath("//button[@onclick='showInput();'][1]").click()  # if there is more than one element

text_result = driver.find_element_by_id("display").text  # Give me the text of the element

text_input = driver.find_element_by_id("user-message").get_attribute("value")  # Gives me the input the user entered

if text_input == text_result:
    print("The text input and text result are equals")

driver.find_element_by_id('sum1').send_keys("7")
driver.find_element_by_id('sum2').send_keys("2")

driver.find_element_by_xpath("//*[text()='Get Total']").click()
