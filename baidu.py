from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# 如果 chromedriver 不在 PATH 中，取消下一行的注释，并改为你的实际路径
# service = Service(executable_path='C:/path/to/chromedriver.exe')
# driver = webdriver.Chrome(service=service)
# 如果已配置 PATH，则直接使用下面这行
driver = webdriver.Chrome()

try:
    print("正在打开百度...")
    driver.get("https://www.baidu.com")
    time.sleep(1)  # 等待页面加载

    # 定位搜索框（修正后的 XPath）
    search_box = driver.find_element(By.XPATH, "//*[@id='kw']")
    print("找到搜索框")
    search_box.send_keys("软件测试")

    # 定位搜索按钮
    search_button = driver.find_element(By.XPATH, "//*[@id='su']")
    print("找到搜索按钮")
    search_button.click()

    print("点击成功，等待3秒...")
    time.sleep(3)
    print("自动化搜索执行成功！")

except Exception as e:
    print("发生错误：", e)   # 打印具体错误信息，方便排查

finally:
    # 注意：如果你想看到浏览器停留，可以注释掉下面这行
    driver.quit()
    print("浏览器已关闭")