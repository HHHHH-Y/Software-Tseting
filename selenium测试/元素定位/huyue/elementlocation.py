from selenium import webdriver
import time


driver = webdriver.Chrome()  # 使用 webDriver 打开 Chrome 浏览器
driver.get("https://www.baidu.com/")  # 输入百度网址

# 最大化浏览器
driver.maximize_window()
time.sleep(3)

# 使用属性进行定位的时候, 这个对象的属性必须是唯一的

# 使用 id 定位
# driver.find_element_by_id("kw").send_keys("吴亦凡")
# driver.find_element_by_id("su").click()

# 使用 name 定位 (不是所有的元素都是有 name 属性的)
# driver.find_element_by_name("wd").send_keys("迪丽热巴")
# driver.find_element_by_id("su").click()

# 使用 class name 定位, 定位失败, 因为 class name 中的内容有多个, 所以无法定位
# driver.find_element_by_class_name("s_ipt").send_keys("林一")
# driver.find_element_by_class_name("btn self-btn bg s_btn btn_h btnhover").click()

# 使用 tag name 定位 定位失败, 因为使用 tag name 定位到的东西太多了, 无法区分是哪一个
# 使用 tag name 的前提是: tag name 唯一
# driver.find_element_by_tag_name("input").send_keys("龚俊")
# driver.find_element_by_id("su").click()



# 使用 链接/部分链接 进行定位的时候, 链接名一定要是唯一的

# 使用 link text 定位
# driver.find_element_by_link_text("视频").click()

# 使用 partial link text 定位, 通过链接的一部分进行查找
# driver.find_element_by_partial_link_text("视").click()

# 使用 xpath 定位(xpath 是一定可以定位到的)
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("关晓彤")
# driver.find_element_by_xpath("//*[@id='su']").click()

# 使用 css selecter 定位
# driver.find_element_by_css_selector("#kw").send_keys("李现")
# driver.find_element_by_css_selector("#su").click()
# time.sleep(3)


# 清除搜索内容(clear)
# driver.find_element_by_id("kw").clear()
# time.sleep(3)
# 重新搜索
driver.find_element_by_id("kw").send_keys(u"吴亦凡")
# 提交查询内容(submit)
driver.find_element_by_id("su").submit()

# 输出定位元素的内容(text)
# text = driver.find_element_by_xpath("//*[@id='bottom_layer']/div[1]").text
# print("text = " + text)


# 打印 title（driver.title）
# 打印 url（driver.current_url）

time.sleep(6)
driver.quit()