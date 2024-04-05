from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 指定 ChromeDriver 的路径
webdriver_path = 'C:/Users/88698/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# 设置无头模式
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# 初始化 WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service, options=options)

# 访问网页
driver.get('https://web.klokah.tw/ninew/learn.php')

# 假设您想要抓取页面上的某个特定元素，您需要检查该网页的HTML，
# 并找到包含您想要数据的元素的标识（如id、class等）。
# 以下是假设您正在寻找某个特定类名的元素的示例。
# 请根据实际情况调整选择器。
elements = driver.find_elements(By.CSS_SELECTOR, '#nine-learn-title')

for element in elements:
    print(element.text)

driver.quit()
