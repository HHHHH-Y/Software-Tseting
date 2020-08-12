from selenium import webdriver
import time

# 打开 Chrome 浏览器
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.maximize_window()
time.sleep(6)

driver.find_element_by_id("kw").send_keys("吴亦凡")
driver.find_element_by_id("su").click()

# 使用固定时间 (必须要等待给定的固定时间)
# time.sleep(10)
# driver.find_element_by_link_text("吴亦凡(华语影视男演员、流行乐歌手)_百度百科").click()

# 使用智能时间 (如果事件在给定时间内就完成了, 则可以马上执行下一步)
driver.implicitly_wait(10)
driver.find_element_by_link_text("吴亦凡(华语影视男演员、流行乐歌手)_百度百科").click()

time.sleep(6)
driver.quit()