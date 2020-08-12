from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("D:/java课堂代码/selenium2html/checkbox.html")
driver.get(file_path)

driver.maximize_window()
time.sleep(3)

# 定位一组元素
names = driver.find_elements_by_tag_name("input")  # 通过 tag name 定位出一组元素
time.sleep(3)
for name in names:
    if name.get_attribute("type") == "checkbox":
        name.click()
time.sleep(3)
driver.quit()
