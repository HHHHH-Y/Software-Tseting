from selenium import webdriver
import time
import unittest
from ddt import ddt, data, file_data, unpack
import sys, csv

# 实践: 使用数据驱动, 用百度搜索不同的关键字

# 使用数据驱动, 相当于是使用一个变量, 只需要写一个方法, 使用数据驱动传入不同的值, 从而得出不同的结果
# 数据驱动 是 驱动整个方法, 而不是局部的代码

# 写一个读取 txt 文件或者 csv 文件的脚本
def getCsv(file_name) :
    rows = []   # 表示的是添加的最外层的数列
    path = sys.path[0]

    # 打开 data 中的 txt/csv 的文件, 进行读取 (从 txt/csv 中读取数据的过程, 将文件中的数据转换成 ([...], [...]) 的格式)
    with open(path + '/data/' + file_name, 'rt', encoding='utf-8') as f:
        readers = csv.reader(f, delimiter = ',', quotechar = '|')   # 读的规则
        next(readers, None)    # 表示一行一行的读取
        for reader in readers:
            # [二十不惑, 二十不惑_百度搜索]
            temprows = []
            for i in reader:
                temprows.append(i)
            rows.append(temprows)
        return rows

# 如果要使用 ddt 数据驱动, 就需要在 类 上面打上一个 @ddt 的标签
@ddt
class Baidu1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com/"
        self.driver.maximize_window()
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    # 使用数据驱动在百度中搜索不同的关键字   只传入一个参数
    @unittest.skip("skipping")
    @file_data('test_baidu_data.json')  # 读取一个 json 文件
    # @data("吴亦凡", "Lisa", "二十不惑", "kris")
    def test_baidu(self, value):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(6)


    # 使用 txt/csv 中的文件进行数据驱动
    # 由于 getCsv 本来就在这个脚本中, 所以可以通过 * 将 getCsv 前面的路径忽略掉
    @data(*getCsv('test_baidu_data.txt'))
    # (["二十不惑","二十不惑_百度搜索"], ["欢乐颂", "欢乐颂_百度搜索"], ["中国新说唱", "中国新说唱_百度搜索"])

    # 使用数据驱动在百度中搜索不同的关键字   但是传入的参数是两个
    # @unittest.skip("skipping")
    # @data(["吴亦凡", "吴亦凡_百度搜索"], ["Lisa", "Lisa_百度搜索"], ["二十不惑", "二十不惑_百度搜索"])
    @unpack   # 在传入两个或者多个参数的时候, 必须加上 @unpack, 这样可以将实参分别映射到方法中的形参上
    def test_baidu1(self, value, except_value):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys(value)
        driver.find_element_by_id("su").click()
        time.sleep(3)
        self.assertEqual(except_value, driver.title, msg="和预期结果不一样")
        print(except_value)
        print(driver.title)
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()
