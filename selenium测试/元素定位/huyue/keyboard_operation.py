from selenium import webdriver
import time
# 在执行键盘按键事件的时候, 需要导入 Keys 包
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get("http://127.0.0.1:88/biz/user-login.html")
driver.get("https://www.baidu.com/")

driver.maximize_window()
time.sleep(3)

# 键盘按键的用法(tab, enter)
# driver.find_element_by_name("account").send_keys("admin")
# time.sleep(2)
# tab
# driver.find_element_by_name("account").send_keys(Keys.TAB)
# time.sleep(2)
# driver.find_element_by_name("password").send_keys("huyuelover1017")
# time.sleep(2)
# enter
# driver.find_element_by_name("password").send_keys(Keys.ENTER)
# time.sleep(6)


# 键盘组合键的用法
driver.find_element_by_id("kw").send_keys("李现")
driver.find_element_by_id("su").submit()
time.sleep(3)

# ctrl + a 全选
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
time.sleep(3)
# ctrl + x 剪切
driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
time.sleep(3)

driver.quit()