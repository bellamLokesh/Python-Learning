from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sobj = Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=sobj)
driver.get("https://money.rediff.com/index.html")
driver.maximize_window()

#self
#Selects the current node itself

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Sectors')]/self::a").text
# print(text_msg)

# #parent
# # Selects the immediate parent
# #syntax-> //tagname[attribute(value(),/parent::tagname
#
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Sectors')]/parent::span").text
# print(text_msg)

#child
# #12 xpath is there i want to choose 6th one how can i select for below path
# # //a[contains(text(),'Sectors')]/ancestor::div/child::span
#
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Sectors')]/ancestor::div/child::span")
# print(len(text_msg))
#
# #ancestor
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Sectors')]/ancestor::div")
# print(len(text_msg))

#descendant
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Sectors')]/ancestor::div/descendant::div")
# print(len(text_msg))

#following
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Sectors')]/ancestor::div/following::div")
# print(len(text_msg))

#following-sibling
#
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Sectors')]/ancestor::div/following-sibling::div")
# print(len(text_msg))

#preceding
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Sectors')]/ancestor::div/preceding::div")
# print(len(text_msg))
#
#
# # preceding-sibling
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Sectors')]/ancestor::div/preceding-sibling::div")
# print(len(text_msg))
