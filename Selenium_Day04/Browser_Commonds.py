#Browser commonds
#1) close()-> it will close single browser window(driver focused on parent window)
#2) quit()-> it will close multiple browsers at a time(it will kill process)
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@id='PageList2']/div/ul/li[3]/a").click()
driver.find_element(By.XPATH,"//*[@id='HTML16']/div[1]/a").click()

time.sleep(10)
# driver.close()#it will close single browser window(driver focused on parent window)
driver.quit()#it will close multiple browsers at a time(it will kill process)
print("Application run successfully")