#working code

# always prefer relative xpath

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

sobj= Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=sobj)
driver.get("https://www.amazon.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 15)
# #Absolutexpath
# driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("5G mobiles")
# driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input").click()

#
# #relative xpath
# driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']").send_keys("5G mobiles")
# driver.find_element(By.XPATH,"//*[@id='nav-search-submit-button']").click()

#And & or
# and -> both attributes should be correct
#or -> any one attibute should be correct

# driver.find_element(By.XPATH,"//*[@type='text' and @spellcheck='false']").send_keys("5G mobiles")
# driver.find_element(By.XPATH,"//*[@value='Go' or @type='su']").click()
#
# #Contains(), starts-with()
# #Contains()-->>>Selects an element if the attribute contains a partial value.
# #starts-with()-->>Selects an element if the attribute value starts with given text.
# driver.find_element(By.XPATH,"//input[contains(@class,'nav-input nav-progressive-attribute')]").send_keys("5G mobiles")
# driver.find_element(By.XPATH,"//input[starts-with(@value,'Go')]").click()

#text()
# Selects an element based on its exact visible text.
driver.find_element(By.XPATH,"//a[text()='Careers']").click()

