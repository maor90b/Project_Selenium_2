from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome \
    (executable_path=r"C:\Users\Student\Desktop\Selenium\chromedriver.exe")

#driver2 = webdriver.Firefox \
# (executable_path=r"C:\Users\Student\Desktop\Selenium\geckodriver.exe")


driver.get("https://www.google.com/")

driver.implicitly_wait(10) #if the website didn't find the element- deadline

driver.maximize_window() # Enlarges the window

#driver.find_element_by_css_selector(".gLFyf").send_keys("Shvili") # Insert text to search textbox

#driver.find_element_by_css_selector(".gLFyf").send_keys(Keys.ENTER) # Selecting enter like in keyboard

#text = driver.find_element_by_css_selector("div.gb_h:nth-child(1) > a").text # Giving the text of the element


element = driver.find_element(By.CSS_SELECTOR, "div.gb_h:nth-child(1) > a")
print(element.text)


driver.find_element_by_css_selector(".gLFyf").send_keys("Shvili" + Keys.ENTER)  #insert text and click enter


#driver.find_element_by_css_selector(".FPdoLc > center:nth-child(1) > input:nth-child(1)").click() #click on icon search

sleep(2)  # driver sleeping
driver.close()








