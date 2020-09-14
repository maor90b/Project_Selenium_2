from selenium import webdriver
from Selenium_Tests.PageLogin import PageLogin
import time

driver = webdriver.Firefox \
    (executable_path=r"C:\Users\Student\Desktop\geckodriver.exe")

pgLogin = PageLogin(driver)

driver.get("https://www.phptravels.net/admin")
time.sleep(2)


print(pgLogin.title().text)

#login
pgLogin.emailSendKeys("admin@phptravels.com")
pgLogin.passSendKeys("demoadmin")
pgLogin.loginKeyClick()

#wait for login to complete
pgLogin.waitForLogin()

driver.quit()