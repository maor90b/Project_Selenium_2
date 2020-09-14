from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium .common.exceptions import NoSuchElementException

driver = webdriver.Firefox \
    (executable_path= r"C:\Users\Student\Desktop\Selenium\geckodriver.exe")

driver.get("https://www.google.com")

driver.find_element_by_css_selector("input[class='gLFyf gsfi']").send_keys("Youtube" + Keys.ENTER)

driver.find_element_by_css_selector("div.g:nth-child(1) > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(2) > span:nth-child(1)").click()

driver.find_element_by_css_selector("input#search").send_keys("Wrecking Ball" + Keys.ENTER)

driver.find_element_by_css_selector("yt-formatted-string[aria-label='Miley Cyrus - Wrecking Ball (Official Video) by Miley Cyrus 6 years ago 3 minutes, 42 seconds 1,089,748,020 views']").click()

