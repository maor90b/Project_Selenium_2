from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

'''Ex 3'''


driver = webdriver.Chrome \
    (executable_path=r"C:\Users\Student\Desktop\Selenium\chromedriver.exe")

driver.implicitly_wait(10)

wait = WebDriverWait(driver, 100)

driver.get("https://www.phptravels.net/admin")

driver.maximize_window()

driver.find_element_by_xpath("//input[@name='email'][1]").send_keys("admin@phptravels.com")

#driver.find_element_by_xpath("//input[@name='password']")
driver.find_element_by_css_selector("input[type='password']").send_keys("demoadmin")

driver.find_element_by_xpath("//button[@type='submit']").click()

driver.find_element_by_css_selector("button[data-target='#quickbook']").click()

wait.until(EC.visibility_of_element_located \
        ((By.ID, "apply")))
#driver.find_element_by_id("apply").send_keys("Yes")
select1 = Select(driver.find_element_by_id("apply"))
select1.select_by_visible_text('Yes')  # Fix that

driver.find_element_by_id("servicetype").send_keys("Hotels")

# driver.find_element_by_css_selector("button[class='btn btn-primary'][type='submit']").click()
driver.find_element_by_xpath('//div[@class="modal-footer"]/button[2]').click()

select= Select(driver.find_element_by_id("selusertype"))
select.select_by_visible_text("Registered")
#driver.find_element_by_id("selusertype").send_keys("Registered")

driver.find_element_by_xpath("//a[@onclick='return false;'][1]").click()

wait.until(EC.visibility_of_element_located \
            ((By.XPATH, "//div[text()='Demo User - user@phptravels.com']")))

driver.find_element_by_xpath("//div[text()='Demo User - user@phptravels.com']").click()

driver.find_element_by_xpath("//input[@placeholder='Date'][1]").click()

#table = driver.find_element_by_xpath("//table[@class=' table-condensed'][1]") # Fix...

driver.find_element_by_xpath("//th[@class='switch']").click()

wait.until(EC.visibility_of_element_located \
               ((By.XPATH, "//td[@colspan='7'][1]")))

months_table = driver.find_element_by_xpath("//td[@colspan='7'][1]")

mydate = datetime.now()
today_month = mydate.strftime("%B")

months = months_table.find_elements_by_tag_name("span")

for month in months:
    if month.text == today_month[0:3]:
        month.click()
        break
    else:
        continue

table = driver.find_element_by_xpath("//table[@class=' table-condensed'][1]")



driver.close()








# rows = monthpicker_Table.find_elements_by_tag_name("tr")
#
# for row in rows:
#     element = row.find_element_by_xpath("//th[@class='switch']")





























