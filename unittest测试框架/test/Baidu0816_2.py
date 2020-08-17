from selenium import webdriver
import time
import unittest

class Baidu2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def teatDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_hao(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("新闻").click()
        time.sleep(6)

    # 忽略测试用例执行
    @unittest.skip("skipping")
    def test_baidusearch(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("花千骨")
        driver.find_element_by_id("su").click()
        time.sleep(6)

if __name__ == "__main__":
    unittest.main()