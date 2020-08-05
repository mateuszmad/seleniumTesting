from selenium import webdriver

driver = webdriver.Chrome(executable_path= "E:\Python\Chromedriver\chromedriver.exe")
driver.get("http://google.pl")

assert "Google" in driver.title

driver.implicitly_wait(10)
