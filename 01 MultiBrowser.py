from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path = "E:\Python\Chromedriver\chromedriver.exe")

driver.get("https://google.com")

print(driver.title) #print title of the page
print(driver.current_url) #print url
print(driver.page_source) #HTML 
driver.close() #close the browser