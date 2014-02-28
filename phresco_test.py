from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "localhost:2468"
username = "nagarajan_s"
password = "Naga5491"
mydriver=webdriver.Firefox()
mydriver.get(baseurl)
xpaths = { 'usernameTxtBox' : "//input[@id='username']",
            'passwordTxtBox' : "//input[@id='password']",
            'submitButton' :   "//input[@id='login']"
          }
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear() 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username) 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear() 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password) 
mydriver.find_element_by_xpath(xpaths['submitButton']).click()            