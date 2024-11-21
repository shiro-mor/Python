from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# 设置浏览器驱动（以 Chrome 为例）
driver = webdriver.Chrome(executable_path='C:\Program Files\chromedriver-win64\chromedriver.exe')  # 替换为你的 ChromeDriver 路径

# 打开网页
url = 'https://www.baidu.com'
driver.get(url)

# 等待页面加载
# time.sleep(3)
try:
    while True:
        # 找到按钮并点击（根据按钮的特性修改选择器）
        search_box = driver.find_element("id", "kw")  # 替换为目标按钮的 XPATH
        try:
            button = driver.find_element(By.XPATH, "//input[@id='s']")  # 替换为目标按钮的 XPATH
        except:
            button = driver.find_element(By.XPATH, "//input[@id='su']")  # 替换为目标按钮的 XPATH
        search_box.clear()  # 清空搜索框
        search_box.send_keys(random.random().__str__());  # 输入随机数
        # button.click()
except KeyboardInterrupt:
    print("KeyboardInterrupt")
finally:
    # 等待一段时间以便观察
    time.sleep(5)

    # 关闭浏览器
    driver.quit()
