# from selenium import webdriver 
from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager 
# from selenium.webdriver.chrome.options import Options  
# import pdb; pdb.set_trace()
from selenium.webdriver.common.action_chains import ActionChains
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
# driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe', chrome_options=options)

from decimal import *
from re import sub
from selenium.webdriver import Firefox
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# import logindata

import os, sys
import time,requests
from bs4 import BeautifulSoup

driver = Firefox(executable_path = 'D:\\Django\\geckodriver.exe')
driver.maximize_window()
action = ActionChains(driver)
sleep(1)

# usr=input('Enter Email Id:')  
# pwd=input('Enter Password:')
usr = '8818993022'
pwd = 'anupam@3022'

driver.get('https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&') 
print ("Opened Amazon ")
sleep(1)

# FirstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[2]')
# action.move_to_element(FirstLevelMenu).perform()
# time.sleep(3)

# SecondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
# SecondLevelMenu.click()
# time.sleep(3)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(usr)
time.sleep(1)

count = driver.find_element_by_xpath('//*[@id = "continue"]')
count.click()
time.sleep(1)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(pwd)
time.sleep(1)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(1)
import pdb; pdb.set_trace()
driver.find_element_by_xpath('/html/body/div[1]/header/div/div[5]/div[2]/div/div/a[1]').click();
driver.find_element_by_xpath('//*[@id="AllGiftCards"]/span/a/div[2]/span').click();
driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div/div/div[1]/div/div/a/img').click();
driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[1]/div/div[1]/div[6]/div/div/div[2]/div[3]/div/div/a/img').click();
amount = input("ENTER YOUR AMOUNT:  ")
amountfilled = driver.find_element_by_xpath('//*[@id="gc-order-form-custom-amount"]')
amountfilled.send_keys(amount)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="gc-delivery-mechanism-button-Email-announce"]').click();
Email = input("ENTER Recievers_Email:  ")
Emailfilled = driver.find_element_by_xpath('//*[@id="gc-order-form-recipients"]').send_keys(Email)
quantity = input("ENTER quantity :  ")
quantityfilled = driver.find_element_by_xpath('//*[@id="gc-order-form-quantity"]').send_keys(quantity)
driver.find_element_by_xpath('//*[@id="gc-buy-box-bn"]').click()
driver.find_element_by_xpath('//*[@id="pp-HzAHGm-94"]/div/div/div/div').click()
card_name = input("Enter Your CardName:  ")
card_number = input("Enter your Card_Number :  ")

driver.find_element_by_xpath('//*[@id="pp-0QaakB-113"]').send_keys(card_name)
driver.find_element_by_xpath('//*[@id="pp-0QaakB-113"]').send_keys(card_number)
'''price=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/div[1]/div/div[2]/span')
Price=price.text
value = Decimal(sub(r'[^\d.]', '', Price))
print(value)
j= 10
if value < j:
   driver.find_element_by_xpath('//*[@id="AddGiftCard"]/div[2]/span/a').click();
else:
    driver.find_element_by_xpath('//*[@id="MobileRecharge"]/span/a/div[2]/span').click();
'''


