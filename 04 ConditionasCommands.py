from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "E:\Python\Chromedriver\chromedriver.exe")

driver.get("https://rozklad-pkp.pl")

time.sleep(5)

ele = driver.find_element_by_id("from-station")
print(ele.is_displayed())
print(ele.is_enabled())

ele.send_keys("Krakow")

odjazd = driver.find_element_by_id("odj")
print("Odjazd zaznaczony = ", odjazd.is_selected())

przyjazd = driver.find_element_by_id("prz")
print("Przyjazd zaznaczony = ", przyjazd.is_selected())

przyjazd.send_keys(Keys.RETURN)

odjazd = driver.find_element_by_id("odj")
print("Odjazd zaznaczony = ", odjazd.is_selected())

przyjazd = driver.find_element_by_id("prz")
print("Przyjazd zaznaczony = ", przyjazd.is_selected())
