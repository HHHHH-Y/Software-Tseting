from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.maximize_window()
time.sleep(6)
driver.find_element_by_id("kw").send_keys("吴亦凡")
driver.find_element_by_id("su").click()
time.sleep(6)

# 打印 title 或者 URL
# 打印出 title (driver.title)
title = driver.title
print("title = " + title)

# 打印出 URL (driver.current_url)
url = driver.current_url
print("url = " + url)

time.sleep(6)
driver.quit()