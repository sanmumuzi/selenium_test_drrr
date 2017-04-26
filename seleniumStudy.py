from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get('http://drrr.com')
assert "DRRR" in browser.title
elem = browser.find_element_by_name('name')
elem.send_keys("竜之峰帝人#dimengyan3mu")
elem.send_keys(Keys.RETURN)
browser.implicitly_wait(2)
browser.find_element_by_xpath('//*[@id="rooms-filter-support"]/ul/li/form/button[@value="fMCejHcO25"]').click()
elem1 = browser.find_element_by_tag_name('textarea')
while True:
    elem1.send_keys("滑稽----这是一个自动程序脚本")
    elem1.send_keys(Keys.RETURN)
    elem1.clear()
    time.sleep(600)