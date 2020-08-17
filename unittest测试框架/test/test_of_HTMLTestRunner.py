import unittest
import os
import sys
import time
import HTMLTestRunner


# 编写一个 HTML 的测试报告

# 生成一个测试套件
def createsuite():
    discovers = unittest.defaultTestLoader.discover("../test", pattern="Baidu*.py", top_level_dir=None)
    print(discovers)
    return discovers


if __name__ == "__main__":

    # 第一步: 首先创建一个专门存放测试报告的文件夹

    # sys.path 是 python 的搜索模块路径集, 返回的结果是一个数组
    curpath = sys.path[0]
    print(sys.path)
    print("=============")
    print(curpath)
    # 如果 resultreport 文件夹不存在, 就需要创建文件夹 resultreport
    # if os.path.exists(curpath + '/resultreport'):
    #     os.makedirs(curpath + '/resultreport')

    if not os.path.exists('./resultreport'):
        os.makedirs('./resultreport')

    # 第二步: 使得 HTML 报告名称不一样 (根据时间去确定报告名称)

    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
    print("---------------------")
    print(time.time())
    print("---------------------")
    print(time.localtime(time.time()))
    print("---------------------")
    print(now)
    filename = curpath + '/resultreport/' + now + 'resultreport.html'
    with open(filename, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行结果",
                                               verbosity=2)
        suite = createsuite()
        runner.run(suite)

    # now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
    # print("-------------")
    # print(time.time())
    # print("-------------")
    # print(time.localtime(time.time()))
    # print("-------------")
    # print(now)
    # # 拼接 HTML 报告的名称
    # filename = curpath + '/resultreport/' + now + '/resultreport.html'
    # with open(filename, 'wb') as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例执行结果",
    #                                            verbosity=2)
    #     suite = createsuite()
    #     runner.run(suite)
