# 上传文件操作
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_name = "file:///" + os.path.abspath("D:/java课堂代码/selenium2html/upload.html")
driver.get(file_name)
driver.maximize_window()
time.sleep(3)

# 定位上传文件按钮
driver.find_element_by_name("file").send_keys("D:/java课堂代码/selenium2html/checkbox.html")

time.sleep(3)
driver.quit()