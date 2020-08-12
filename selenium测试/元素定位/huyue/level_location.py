from selenium import webdriver
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("D:/java课堂代码/selenium2html/level_locate.html")
driver.get(file_path)

driver.maximize_window()

# 层级定位
time.sleep(3)
driver.find_element_by_link_text("Link1").click()
time.sleep(3)
target = driver.find_element_by_link_text("Another action")
# 鼠标事件, 移动鼠标到目标元素
ActionChains(driver).move_to_element(target).perform()
time.sleep(3)
driver.quit()