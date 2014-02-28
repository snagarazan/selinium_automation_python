from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = "https://www.gmail.com"
username = "snaga042"
password = "N@G@5491"
mydriver=webdriver.Firefox()
mydriver.get(baseurl)
xpaths = { 'usernameTxtBox' : "//input[@id='Email']",
            'passwordTxtBox' : "//input[@id='Passwd']",
            'submitButton' :   "//input[@id='signIn']"
          }


# baseurl = "https://www.facebook.com"
# username = "santhoshkumar2602@gmail.com"
# password = "TimeEater"
# mydriver = webdriver.Firefox()
# mydriver.get(baseurl)

# xpaths = { 'usernameTxtBox' : "//input[@id='email']",
#            'passwordTxtBox' : "//input[@id='pass']",
#            'submitButton' :   "//button[@id='loginbutton']"
#          }
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear() 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username) 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear() 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password) 
mydriver.find_element_by_xpath(xpaths['submitButton']).click()
mydriver.find_element_by_id("//div/div[2]/div[5]/div/a").click()
  
#mydriver.find_element_by_selector("//div/div[2]/div[5]/div/a").click()
#mydriver.quit()
