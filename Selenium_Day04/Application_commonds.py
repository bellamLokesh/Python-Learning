#Application commonds

#these functions or commonds will be work with "driver"
# 1) get()->> is used to open current url
# 2) tittle()->> is used to captured current tittle of the webpage
# 3)current_url()->> is used to captured the current url of the webpage
# 4)page_)source()->> is used to captured current source code of the webpage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
print(driver.title)#Automation Testing Practice
print(driver.current_url)#https://testautomationpractice.blogspot.com/
print(driver.page_source)# it will return the all the source code of the webpage

driver.quit()