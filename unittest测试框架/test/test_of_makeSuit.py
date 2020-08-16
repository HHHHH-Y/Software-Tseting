import unittest
from test import Baidu0816_1
from test import Baidu0816_2

# 使用 makeSuite() 将测试方法加到测试套件中
# makeSuite() 可以将 一个测试类中的所有测试方法 都 加入到测试套件中
# suite. addTest(unittest.makeSuite(文件名.类名))


def createSuite() :

    suite = unittest.TestSuite()

    # 使用 makeSuit() 将 一个类中的所有测试用例加入到测试套件 suit 中
    suite.addTest(unittest.makeSuite(Baidu0816_1.Baidu1))
    suite.addTest(unittest.makeSuite(Baidu0816_2.Baidu2))
    return suite

if __name__ == "__main__":
    suite = createSuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)