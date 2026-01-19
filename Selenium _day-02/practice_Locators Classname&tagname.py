# #Task-01
# # 🎯 Find using CLASS_NAME:
# #
# # 1️⃣ Login button
# # 2️⃣ Username input
# # 3️⃣ Password input
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# service_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
# driver.find_element(By.CLASS_NAME,"oxd-input oxd-input--active").send_keys("Admin")
# driver.find_element(By.CLASS_NAME,"oxd-input oxd-input--active").send_keys("admin123")
# driver.find_element(By.CLASS_NAME,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
# driver.close()
# print("code runs succesfully")

# #Task-02
# https://www.facebook.com/
#
# 🎯 Find using CLASS_NAME:
#
# 1️⃣ Email textbox
# 2️⃣ Password textbox
# 3️⃣ Login button

#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# service_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get("https://www.facebook.com/")
# driver.find_element(By.CLASS_NAME,"inputtext").send_keys("lokeshtarak")
# driver.find_element(By.CLASS_NAME,"_6luy").send_keys("9876456566")
# driver.find_element(By.CLASS_NAME,"_42ft").click()
#
# driver.close()
# print("code runs succesfully")

# #Task-03
# 🌐 https://www.wikipedia.org/
#
# 🎯 Find using TAG_NAME:
#
# 1️⃣ Count how many <a> tags are present
# 2️⃣ Count how many <input> tags
# 3️⃣ Print counts in console


#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# service_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver=webdriver.Chrome(service=service_obj)
# driver.get("https://www.wikipedia.org/")
# anchor = driver.find_elements(By.TAG_NAME,"a")
# print(len(anchor))
# anchor1 = driver.find_elements(By.TAG_NAME,"input")
# print(len(anchor1))
# driver.close()
# print("code runs succesfully")

# #task-04:
#
# https://testautomationpractice.blogspot.com/
#
# 🎯 Find using TAG_NAME:
#
# 1️⃣ Count number of input tags
# 2️⃣ Count number of button tags


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
anchor = driver.find_elements(By.TAG_NAME,"input")
print(len(anchor))
anchor1 = driver.find_elements(By.TAG_NAME,"button")
print(len(anchor1))
driver.close()
print("code runs succesfully")
