import unittest
from test import Baidu0816_1
from test import Baidu0816_2

# discover() 可以将 一个文件夹下 某种命名规则的文件中的所有测试方法 都加入到一个测试套件中
# discovers = unittest.defaultTestLoader.descover("进入要加的文件夹", pattern="要加入的测试文件的样式", top_level_dir=None)

def createsuite():
    # 第一个参数: "../test": 从当前文件回到上一级目录, 并去到想要加入测试套件的文件夹下
    # 第二个参数: pattern="Baidu*.py": 将这个文件夹下, 以 Baidu 开头, .py 结尾的所有测试文件都加入到测试套件中
    # 第三个参数: top_lever_dir=None: 固定格式的写法
    discovers = unittest.defaultTestLoader.discover("../test", pattern="Baidu*.py", top_level_dir=None)
    print(discovers)
    return discovers


if __name__ == "__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)