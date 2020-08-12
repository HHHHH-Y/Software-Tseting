from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

# 对浏览器的操作
# 浏览器最大化
driver.maximize_window()
time.sleep(3)

driver.find_element_by_id("kw").send_keys("吴亦凡")
driver.find_element_by_id("su").submit()
time.sleep(6)

# 浏览器最小化
driver.minimize_window()
time.sleep(3)

driver.maximize_window()
time.sleep(3)

# 设置浏览器的宽, 高
driver.set_window_size(480, 800)
time.sleep(3)

driver.maximize_window()
time.sleep(2)

# 操作浏览器的后退, 前进
# 后退
driver.back()
time.sleep(3)
# 前进
driver.forward()
time.sleep(3)

# 控制浏览器的滚动条
# 向后滚
js = "var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
time.sleep(3)

# 向前滚
js1 = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js1)
time.sleep(3)
driver.quit()