from selenium import webdriver
import time
import os
driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath("D:/java课堂代码/selenium2html/drop_down.html")
driver.get(file_path)

driver.maximize_window()
time.sleep(3)

# 下拉框的处理和定位

# 1. 定位一组元素. 然后遍历进行条件筛选
# names = driver.find_elements_by_tag_name("option")
# time.sleep(3)
# for name in names:
#     if name.get_attribute("value") == "9.25":
#         name.click()

# 2. 利用数组的下标进行定位
# names = driver.find_elements_by_tag_name("option")
# names[3].click()

# 3. 使用 Xpath 去定位
# driver.find_element_by_xpath("//*[@id='ShippingMethod']/option[4]").click()

# 4. 使用 CSS selector 进行定位
driver.find_element_by_css_selector("#ShippingMethod > option:nth-child(4)").click()

time.sleep(3)

driver.quit()