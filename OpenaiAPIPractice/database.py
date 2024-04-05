from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# 指定 ChromeDriver 的路径
webdriver_path = 'C:/Users/88698/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe'

# 设置无头模式
#options = webdriver.ChromeOptions()
#options.add_argument('--headless')

# 初始化 WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# 访问网页
driver.get('https://web.klokah.tw/ninew/learn.php')

# 假设您想要抓取页面上的某个特定元素，您需要检查该网页的HTML，
# 并找到包含您想要数据的元素的标识（如id、class等）。
# 以下是假设您正在寻找某个特定类名的元素的示例。
# 请根据实际情况调整选择器。

# 找到要点击的元素，并点击它
step1 = driver.find_element(By.CSS_SELECTOR, 'div.switcher')
step1.click()
time.sleep(3)

step2 = driver.find_element(By.CSS_SELECTOR, "a.language[lid='5']")
step2.click()
time.sleep(3)

step3 = driver.find_element(By.CSS_SELECTOR, "a.dialect[did='17']")
step3.click()
time.sleep(3)

step4 = driver.find_element(By.CSS_SELECTOR, "a.nine-level-btn[id='nine-level-1']")
step4.click()
time.sleep(3)

step5 = driver.find_element(By.CSS_SELECTOR, "a.nine-class-btn[id='nine-class-1']")
step5.click()
time.sleep(3)

elements = driver.find_elements(By.CSS_SELECTOR, '.lesson-text')
#print(elements)

for element in elements:
    print(element.text)



driver.quit()
