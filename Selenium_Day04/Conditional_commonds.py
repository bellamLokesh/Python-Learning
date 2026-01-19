#Conditional commonds alwya returns boolen values true or false.
# before we need to impliment conditional commonds we need to find element later on we need to apply conditional commonds
#1) is_displayed->>used for any element it will check particular element is displayed in current webpage or not
#2) is_enabled->> used for any element it will check whther the element is allowing text or not
#3) is_selcted->> used only for radio buttons eg, male or female, check boxes


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://testautomationpractice.blogspot.com/")
# #is_displayed
# udemy=driver.find_element(By.XPATH,"//*[@id='PageList2']/div/ul/li[2]/a")
# print("displayed statues:",udemy.is_displayed())#True
# #is_displyed() & is_enabled
# entername=driver.find_element(By.XPATH,"//*[@id='name']")
# print("display status:",entername.is_displayed())#True
# print("enable status:",entername.is_enabled())#True
#is_selcted
male_radiobutton = driver.find_element(By.XPATH, "//*[@id='male']")
female_radiobutton = driver.find_element(By.XPATH, "//*[@id='female']")
print("defalut radio buttons status")
print(male_radiobutton.is_selected())  #False
print(female_radiobutton.is_selected())  #False
print("after selcting male radio button status")
male_radiobutton.click()  #after selcting radio button
print(male_radiobutton.is_selected())  #True
print(female_radiobutton.is_selected())  #False
driver.quit()
