#task-01
# 🌐 https://opensource-demo.orangehrmlive.com/
#
# Use ONLY CSS_SELECTOR
#
# 1️⃣ Username → attribute selector
# 2️⃣ Password → attribute selector
# 3️⃣ Login button → tag + attribute
# 4️⃣ Forgot password → class selector

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

servc_obj=Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=servc_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"[name=username]").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"[type=password]").send_keys("admin123")

driver.close()
print("code successfully run")
