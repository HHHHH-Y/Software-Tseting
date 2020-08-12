from selenium import webdriver
import time
# 在执行鼠标事件时需要导 ActionChains 包
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.maximize_window()
time.sleep(3)

driver.find_element_by_id("kw").send_keys("吴亦凡")
driver.find_element_by_id("su").click()
time.sleep(3)

# 鼠标事件
# 右击
su = driver.find_element_by_id("su")
ActionChains(driver).context_click(su).perform()
time.sleep(3)
# 双击
su = driver.find_element_by_id("su");

time.sleep(3)
driver.quit()