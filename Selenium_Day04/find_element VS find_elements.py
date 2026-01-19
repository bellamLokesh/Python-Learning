#1-->>>find_element():

#
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.snapdeal.com/")
# time.sleep(10)
# driver.maximize_window()
# # Scenario-01>>>> locator matching with single web element
# # search_variable=driver.find_element(By.XPATH,"//*[@id='search-box-input']")
# # search_variable.send_keys("kitchen items")
# # time.sleep(5)
#
# # Scenario-02>>>> locator matching with multiple web element
# #here i mentioned xpath that shows 20 elements but it will print only first element why becuse uw used find_element here.
# # links=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[8]/div[1]//a")
# # print(links.text)#print first link from the footer map"Privacy Policy"
# #
# # # #Scenario-03>>> element not avilable then throw Nosuchelementexception
# # #Login- Correct linktext for "login"
# # login_variable=driver.find_element(By.LINK_TEXT,"My Cart")
# # login_variable.click()
#
# print("codes runs")
#


#02-->>>find_elements() it will return multiple webelements



import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.snapdeal.com/")
time.sleep(5)
driver.maximize_window()

## # Scenario-01>>>> locator matching with single web element
# find_elements() is a collection of list of elements
# here i used find_elements but actual that locator i mentioned is locating only one element but find_elements woill never throw exception
# # it will  print that single web element
# search_variable=driver.find_elements(By.XPATH,"//*[@id='search-box-input']")
# print(len(search_variable))#1
# search_variable[0].send_keys("kitchen items")# here i am entering text by accisng through index o and iam using senkeys method to enter text
# time.sleep(5)
#
# # Scenario-02>>>> locator matching with multiple web element
# links = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div[8]/div[1]//a")
# print(len(links))#20 -> it will returns the count of links inside the footer
# print(links[5].text)#Products Under Cumpulsory BIS Certification -> whatever is avialble in 5th index text is copying by using list index
#
# for element in links :
#     print(element.text)
#
#
# #output: by using loop we can print all 20 footer link text
# # Privacy Policy
# Terms of Sale
# Terms of Use
# Report Abuse & Takedown Policy
# Know Your BIS Standard
# Products Under Cumpulsory BIS Certification
# FAQ
# About Us
# Careers
# Blog
# Sitemap
# Contact Us
# Shopping App
# Sell on Snapdeal
# Media Enquiries
# Lehenga
# Kid's Clothing
# Sarees
# Winter Wear
# Sweatshir


# # # #Scenario-03>>> element not avilable then throw Nosuchelementexception
# # #Login- Correct linktext for "login"
login_variable=driver.find_elements(By.LINK_TEXT,"My Cart")
print("elements returned:",len(login_variable))#0 -> even though if elements is not avialble find_elements() never thrown an exception it will run succesfully
print("code runs")
