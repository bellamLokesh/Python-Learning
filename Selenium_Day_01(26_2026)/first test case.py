# from selenium import webdriver
# from selenium.webdriver.Chrome.service import service
# from selenium.webdriver.common.by import By
#
# servc_obj=service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver=webdriver.chrome(Service=servc_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.find_element(By.NAME,"username").send_keys("Admin")
# driver.find_element(By.TYPE,"password").send_keys("admin123")
# driver.find_element(By.CLASS,"oxd-form-actions orangehrm-login-action").click
# actual_tittle=driver.tittle
# expected_tittle="OrangeHRM"
#
# if actual_tittle==expected_tittle:
#     print("Login Test passed")
# else:
#     print("Login test failed ")
#
# driver.close()



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ChromeDriver path
service_obj = Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")

# Launch browser
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()

# Open URL
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button']").click()

time.sleep(3)

# Title validation
actual_title = driver.title
expected_title = "OrangeHRM"

if actual_title == expected_title:
    print("✅ Login Test Passed")
else:
    print("❌ Login Test Failed")

driver.quit()
