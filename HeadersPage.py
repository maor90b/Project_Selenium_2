from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from time import sleep

class PageHeaders():
    def __init__(self, driver):
        self.driver = driver

    def UserIconClick(self):
        self.driver.find_element_by_id("menuUser").click()

    def UsernameSendKeys(self, username):
        self.driver.find_element_by_name("username").send_keys(username)

    def PassWordSendKeys(self, password):
        self.driver.find_element_by_name("password").send_keys(password)

    def SignInClick(self):
        self.driver.find_element_by_id("sign_in_btnundefined").click()

    def Cart(self):
        self.driver.find_element_by_id("menuCart")

    def MouseOnIconCart(self):
        element = self.driver.find_element_by_id("menuCart")
        actionChains = ActionChains(self.driver)
        actionChains.move_to_element(element).perform()

    def CartClick(self):
       WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable \
                                                ((By.ID, "menuCart")))
       self.driver.find_element_by_id("menuCart").click()

    def Cart_Quantity(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located \
                                                 ((By.XPATH, "//label[@class='roboto-regular ng-binding'][1]")))
        return self.driver.find_element_by_xpath("//label[@class='roboto-regular ng-binding'][1]").text

    def Cart_Details(self):
        # table = self.driver.find_element_by_css_selector("table>tbody")
        # rows = table.find_elements_by_tag_name("tr")
        # products_details={}
        # i=1
        # for row in rows:
        #     name = row.find_element_by_xpath("//a/h3[@class='ng-binding']").text
        #     quantity = row.find_element_by_xpath("//label[contains(text(), 'QTY')]").text
        #     color = row.find_element_by_xpath("//label[@class='ng-binding']/span").text
        #     price = row.find_element_by_xpath("//p[@class='price roboto-regular ng-binding']").text
        #     products_details[i]= f'Name= {name} ,Color= {color},Quantity= {quantity},Price= {price}'
        #     i+= 1
        # return products_details


        table = self.driver.find_element_by_css_selector('ul>li>tool-tip-cart>div>table>tbody')
        rows = table.find_elements_by_tag_name('tr')
        products = {}
        i=1
        for row in rows:
            name = row.find_element_by_css_selector('tbody>tr>td>a>h3').text
            QTY = row.find_element_by_css_selector('tbody>tr>td>a>label').text
            color = row.find_element_by_css_selector('tbody>tr>td>a>label>span').text
            price = row.find_element_by_css_selector('tbody>tr>td>p').text
            products[i]= (f'Name= {name} ,Color= {color},Quantity= {QTY},Price= {price}')
            i+=1
        return products

















