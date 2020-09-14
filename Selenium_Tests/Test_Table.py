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

driver.get("http://www.seleniumeasy.com/test/table-search-filter-demo.html")

table = driver.find_element_by_id("task-table")

rows = table.find_elements_by_tag_name("tr")

for row in rows:
    cells = row.find_elements_by_tag_name("td")  # Each row has few fields

    for cell in cells:
        print(cell.text)

driver.close()
