from selenium import webdriver
from selenium.webdriver.common.by import By
from AOS_Selenium.Main_AOS import MainPage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome \
    (executable_path=r"C:\Users\Student\Desktop\Selenium\chromedriver.exe")

driver.get("https://www.advantageonlineshopping.com/#/")

driver.implicitly_wait(10)

AOS = MainPage(driver)

AOS.ClickCategory("Tablets")
driver.maximize_window()

Tab =
sleep(2)
driver.quit()









