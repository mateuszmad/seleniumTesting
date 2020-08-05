from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("E:\Python\Chromedriver\chromedriver.exe")

driver.get("http://google.com")

print(driver.title)

driver.get("http://onet.pl")
time.sleep(2)

print(driver.title)

driver.back()

time.sleep(2)
print(driver.title)

driver.forward()

print(driver.title)

driver.quit()