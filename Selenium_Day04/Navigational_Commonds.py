# # Navigational Commonds: used to control the browser's navigation.
#
# #1) back()---->>>go to previous page in the browser history. Same as "Back" button in the browser.
# #2) forward()----->>go to next page in the browser history. Same as "Forward" button in the browser.
# #3) refresh()----->>>reloads the current page. Same as the "Refresh" button in the browser.
#
#
#
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service_obj = Service("C:/Users/User/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.snapdeal.com/")
# time.sleep(5)
# driver.maximize_window()
# driver.get("https://www.amazon.com/")
# time.sleep(5)
# driver.back()
# time.sleep(5)
# driver.forward()
# time.sleep(5)
# driver.refresh()
# time.sleep(5)
# driver.quit()
#
# print("navigational commonds working fine")
