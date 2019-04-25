import time

#Keyboard Module
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#Opera Browser-setup
from selenium import webdriver
from selenium.webdriver.chrome import service
webdriver_service = service.Service('F:\\SELENIUM\\operadriver_win64\\operadriver.exe')
webdriver_service.start()
driver = webdriver.Remote(webdriver_service.service_url)
driver.get("http://www.thetestingworld.com/testings/")

#Maximizing the Window
driver.maximize_window()

#Working on Keyboard
driver.find_element_by_name('fld_username').send_keys('Hello World')
act = ActionChains(driver)
#act.send_keys(Keys.TAB).perform()
#act.send_keys('qwerty@123').perform()
act.send_keys(Keys.CONTROL).send_keys("a").perform()

#Closing Browser
time.sleep(5)
driver.close()