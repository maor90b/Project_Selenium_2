from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome \
    (executable_path=r"C:\Users\Student\Desktop\Selenium\chromedriver.exe")

driver.implicitly_wait(5)

driver.get("https://www.phptravels.net/admin")

driver.find_element_by_xpath("//input[@name='email'][1]").send_keys("admin@phptravels.com")

# driver.find_element_by_xpath("//input[@name='password']")
driver.find_element_by_css_selector("input[type='password']").send_keys("demoadmin")

driver.find_element_by_xpath("//button[@type='submit']").click()

'''Ex 2'''

WebDriverWait(driver, 10).until(EC.visibility_of_element_located \
             ((By.CSS_SELECTOR, "a[href='https://www.phptravels.net/admin']")))


text = "DASHBOARD"
result_text = driver.find_element_by_css_selector("a[href='https://www.phptravels.net/admin']").text
# result_text= driver.find_element_by_xpath("//li/a/strong").text # Second option

if text == result_text:
    print("The test passed successfully")
    print(result_text)
else:
    print("The test failed")

driver.find_element_by_class_name("fa-sign-out").click()
print("The account logging out")

sleep(5)

driver.back()
driver.close()
