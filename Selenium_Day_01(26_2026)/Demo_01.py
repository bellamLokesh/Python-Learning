from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

# Implict wait
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")
wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("admin123")
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

# 'Actions concept'
actions = ActionChains(driver)
element = driver.findElement(By.Xpath("button"))
actions.double_click(element).perform();
actions.context_click(element).perform();
driver.find_element(By.NAME("Settings")).click()
source = driver.findElement(By.Xpath("source"))
dest = driver.findElement(By.Xpath("destination"))
actions.drag_and_drop(source,dest)

ele1 = driver.find_element(By.NAME("information science"))
actions.move_to_element(ele1).perform()
driver.find_element(By.NAME("chane address")).click()


