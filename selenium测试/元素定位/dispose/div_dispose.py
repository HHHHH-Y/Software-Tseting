# div 模块定位
from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_name = "file:///" + os.path.abspath("D:/java课堂代码/selenium2html/modal.html")
driver.get(file_name)
driver.maximize_window()
time.sleep(3)

# 点击主页的 click 按钮
driver.find_element_by_id("show_modal").click()
time.sleep(3)

# 点击 click me (首先先找到 click me 所在的 div, 然后再进行点击)
div1 = driver.find_element_by_class_name("modal-body")
div1.find_element_by_link_text("click me").click()
time.sleep(3)

# 定位 close (首先定位 close 的 div, 然后再进行点击)
div2 = driver.find_element_by_class_name("modal-foot")
buttons = div2.find_elements_by_tag_name("button")
time.sleep(3)
buttons[0].click()

time.sleep(3)
driver.quit()