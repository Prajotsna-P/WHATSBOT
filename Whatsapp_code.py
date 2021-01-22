from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
#sub
import subprocess
subprocess.call([r'E:\Studies doc\Python\Studypython\chromeLaunch.bat'])
sleep(5)
#"E:\Studies doc\Python\Studypython\chromeLaunch.bat"

#opening chrome in debug mode
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

#chrome_driver = webdriver.Chrome('C:/Chromedriver/chromedriver')
chrome_driver = r"C:/Chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
sleep(15)
print('Code ended its pause.')

user_name = 'Prajo'
inp_xpath_search =  '//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="3"]'
input_box_search = driver.find_element_by_xpath(inp_xpath_search)
input_box_search.click()
sleep(2)
input_box_search.send_keys(user_name)
sleep(2)
user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
user.click()
sub="ssu"
while True:
    p=driver.find_elements_by_class_name('_1RAno')
    for item in p:
        if sub in item.text.lower():
            temp=item.text
            print(temp)
            #code add
    break
    