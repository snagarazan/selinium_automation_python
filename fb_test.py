from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://www.facebook.com"
username = "santhoshkumar2602@gmail.com"
password = "TimeEater"
mydriver=webdriver.Firefox()
mydriver.get(baseurl)
xpaths = { 'usernameTxtBox' : "//input[@id='email']",
            'passwordTxtBox' : "//input[@id='pass']",
            'submitButton' :   "//label[@id='loginbutton']/input",
            'photos':"//li[@id='navItem_app_2305272732']/a/div[2]/div"
          }
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear() 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username) 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear() 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password) 
mydriver.find_element_by_xpath(xpaths['submitButton']).click()  
mydriver.find_element_by_xpath(xpaths['photos']).click()
mydriver.find_element_by_xpath("//div[@id='userNavigationLabel']").click()
mydriver.find_element_by_xpath("//input[@value='Log Out']").click()
# mydriver.quit()
