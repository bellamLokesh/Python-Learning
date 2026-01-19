
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sobj= Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=sobj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 15)
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("Lokesh")
driver.find_element(By.ID,"email").send_keys("abc@gmail.com")
driver.find_element(By.CLASS_NAME,"form-control").send_keys("92772")

