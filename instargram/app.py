from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import pyperclip

from selenium.webdriver.chrome.options import Options

옵션 = webdriver.ChromeOptions()
옵션.add_argument(r'user-data-dir=C:\Program Files (x86)\scoped_dir26984_1492218311\Default')

driver = webdriver.Chrome('chromedriver.exe', chrome_options=옵션)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144&url=http://m.naver.com/aside/')

time.sleep(2)

pyperclip.copy('psw4978')

e = driver.find_element_by_css_selector('#id')
e.send_keys(Keys.CONTROL, 'v')

time.sleep(1)

pyperclip.copy('qwer8456123')

e = driver.find_element_by_css_selector('#pw')
e.send_keys(Keys.CONTROL, 'v')

time.sleep(1)
e.send_keys(Keys.ENTER)

time.sleep(2)
e = driver.find_elements_by_css_selector('.shortcut_a')[2]
e.click()

time.sleep(1)
driver.get('https://blog.editor.naver.com/editor?deviceType=mobile&returnUrl=https%3A%2F%2Fm.blog.naver.com%2FFeedList.naver')

time.sleep(1)
e = driver.find_element_by_css_selector('div[placeholder="내용을 입력하세요."]')
e.click()

pyperclip.copy("안녕하세요 반갑습니다")
e.send_keys(Keys.CONTROL, 'v')

time.sleep(2)
e = driver.find_element_by_css_selector('textarea[placeholder="제목"]')
e.click()

time.sleep(1)
pyperclip.copy("오늘의 제목")
e.send_keys(Keys.CONTROL, 'v')

time.sleep(1)

e = driver.find_element_by_css_selector('button[class="btn_applyPost"]')
e.click()

