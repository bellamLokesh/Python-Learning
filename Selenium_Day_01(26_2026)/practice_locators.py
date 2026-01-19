#tak_01
# TASK 1: OrangeHRM Login Page
#
# 🌐 https://opensource-demo.orangehrmlive.com/
#
# 🎯 Find elements using:
#
# ID → Login button
#
# NAME → Username field
#
# NAME → Password field
#
# LinkText → “Forgot your password?”
#
# Partial LinkText → “Forgot”

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# #
# # service_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
# # driver.find_element(By.XPATH,"//*[@name='username']").send_keys("Admin")
# # driver.find_element(By.XPATH,"//*[@name='password']").send_keys("admin123")
# # driver.find_element(By.XPATH,"//*[@type='submit']").click()
# driver.find_element(By.LINK_TEXT,"orangehrm-login-forgot").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"forgot").click()


# #Task-02:
# 🌐 https://www.google.com/
#
# 🎯 Find elements using:
#
# NAME → Search input box
#
# LinkText → “Gmail”
#
# Partial LinkText → “Gm”
#
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
#
# service_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get("https://www.google.com/")
# driver.maximize_window()
# wait = WebDriverWait(driver,10)
# # driver.find_element(By.NAME,"q").send_keys("prabhas")
# # driver.find_element(By.LINK_TEXT,"Gmail").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Gm").click()
# # print("code run susseccfully")
#
# driver.close()

# #Task-03
#
# 🌐 https://www.facebook.com/
#
# 🎯 Find elements using:
#
# ID → Email / Phone field
#
# ID → Password field
#
# NAME → Login button
#
# LinkText → “Forgotten password?”
#
# Partial LinkText → “Forgot”
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get(" https://www.facebook.com/")
# # driver.find_element(By.ID,"email").send_keys("kurabalokesh")
# # driver.find_element(By.ID,"pass").send_keys("8096155751")
# # driver.find_element(By.NAME,"login").click()
# driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
# # driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten").click()
#
#
# driver.close()
# print("code run susseccfully")


# #Task-04
#
# https://testautomationpractice.blogspot.com/
#
# 🎯 Find elements using:
#
# ID → Name textbox
#
# ID → Email textbox
#
# NAME → Gender radio button
#
# LinkText → “Home”
#
# Partial LinkText → “Selenium”
#

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.ID,"name").send_keys("lokesh")
driver.find_element(By.ID,"email").send_keys("lokesh@abc")
driver.find_element(By.NAME,"gender").click()
driver.find_element(By.LINK_TEXT,"Home").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Selenium").click()

driver.close()
print("code run susseccfully")


# Task-05
#
# https://www.wikipedia.org/
#
# 🎯 Find elements using:
#
# ID → Search input box
#
# NAME → Search input
#
# LinkText → “English”
#
# Partial LinkText → “Eng”

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

S_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=S_obj)
driver.get(" https://www.wikipedia.org/")
driver.find_element(By.ID,"searchInput").send_keys("infosys")
driver.find_element(By.XPATH,"//*[@id='search-form']/fieldset/button").click()
driver.find_element(By.LINK_TEXT,"English").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Eng").click()

driver.close()
print("code run susseccfully")

