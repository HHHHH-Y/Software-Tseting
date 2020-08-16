import unittest
from test import Baidu0816_1
from test import Baidu0816_2

# 使用 addTest() 将测试方法加入到测试套件中
# addTest() 适合将 测试方法 一个一个 的加入到 suite 测试套件中
# suite.addTest(文件名.类名(要加载到套件中的方法名))

# 定义了一个 createsuit 创建套件的方法
def createsuite():

    # 创建一个 suit 测试套件
    suite = unittest.TestSuite()

    # 将测试用例加入到测试套件 suit 中, 使用 addTset()
    suite.addTest(Baidu0816_1.Baidu1("test_hao"))
    suite.addTest(Baidu0816_1.Baidu1("test_baidusearch"))
    suite.addTest(Baidu0816_2.Baidu2("test_baidusearch"))
    # 返回测试套件 suit
    return suite

if __name__ == "__main__":
    # 得到测试套件 suit
    suit = createsuit()
    # 跑测试套件的 runner
    runner = unittest.TextTestRunner(verbosity=2) # 使用 verbosity=2 所打印出来的结果日志更加详细
    runner.run(suit)
