from selenium import webdriver
import time
import unittest

# def 表示的是一个方法
# 每一个方法中, 参数的第一个必须是 self
# 如果定义一个全局变量, 必须使用 self.变量名来定义
class Baidu1(unittest.TestCase):

    # 运行类的前期准备方法
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    # 做一些清理处理, 善后工作
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 以 test_ 开头的方法都是测试方法, 可以自动运行
    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("hao123").click()
        time.sleep(6)

    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("二十不惑")
        driver.find_element_by_id("su").click()
        time.sleep(6)
        self.assertTrue(123 == 1234, msg="not true")

if __name__ == "__main__":
    unittest.main()