from selenium import webdriver
from AOS_Selenium.Main_AOS import MainPage
from time import sleep
from AOS_Selenium.HeadersPage import PageHeaders
from AOS_Selenium.TabletsPage import TabletsPage
from AOS_Selenium.Products_To_Cart import Product_Purchase
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome \
    (executable_path=r"C:\Users\Student\Desktop\Selenium\chromedriver.exe")

driver.get("https://www.advantageonlineshopping.com/#/")

driver.implicitly_wait(10)

driver.maximize_window()

AOS = MainPage(driver)

AOS.ClickCategory("Tablets")

Tab = TabletsPage(driver)

Tab.ClickProduct(1)

Product_1= Product_Purchase(driver)

Product_1.Quantity('1')

Product_1.Click_Add_To_Cart()

driver.back()

Tab.ClickProduct(2)

Product_2 = Product_Purchase(driver)

Product_2.Quantity('2')

Product_2.Click_Add_To_Cart()

driver.back()

Tab.ClickProduct(3)

Product_3 = Product_Purchase(driver)

Product_3.Quantity('3')

Product_3.Click_Add_To_Cart()

Icon_Cart = PageHeaders(driver)

print("Quantity of items cart:",Icon_Cart.Cart_Quantity())

# Icon_Cart.MouseOnIconCart()

print(Icon_Cart.Cart_Details())


# table = driver.find_element_by_css_selector("td[colspan='2']")
#
# rows = table.find_elements_by_tag_name("span")
#
# for row in rows:
#     if row.text == 'TOTAL':
#         driver.find_element_by_xpath(f"'//{row}/label").text
#         break
#     else:
#         continue







# sleep(10)
# driver.close()

