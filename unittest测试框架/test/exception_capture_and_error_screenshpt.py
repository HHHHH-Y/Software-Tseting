# 异常捕捉和错误截图
from selenium import webdriver
import unittest
import time
import os
import re
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

class Baidu3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("二十不惑")
        driver.find_element_by_id("su").click()
        time.sleep(3)

        # 异常捕获
        try:
            self.assertEqual("二十不惑_百度搜索", driver.title, msg="二者不相同")
        except:
            # 如果 try 中的语句发生错误, 则对错误信息进行异常捕获并进行错误截图
            self.saveScreenShot(driver, "baiduError.png") # 对错误进行截图(传入浏览器驱动, 截图的名称和格式)
        time.sleep(3)

    # 错误截图
    def saveScreenShot(self, driver, file_name):
        if not os.path.exists("./errorImage"):
            os.makedirs("./errorImage")
            # 仍然使用时间来进行命名
        now = time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
        driver.get_screenshot_as_file("./errorImage/" + now + "-" + file_name)
        time.sleep(3)
