import time

#Mouse Module
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#Opera Browser-setup
from selenium import webdriver
from selenium.webdriver.chrome import service
webdriver_service = service.Service('F:\\SELENIUM\\operadriver_win64\\operadriver.exe')
webdriver_service.start()
driver = webdriver.Remote(webdriver_service.service_url)
driver.get("http://www.thetestingworld.com/")

#Maximizing the Window
driver.maximize_window()

#Working on Mouse
act = ActionChains(driver)

#Left Click
#act.click().perform()
#time.sleep(2)
#act.click(driver.find_element_by_xpath('//a[text()="login"]')).perform()
#time.sleep(2)

#Right Click
#act.context_click().perform()
#time.sleep(2)
#act.context_click(driver.find_element_by_xpath('//a[text()="Login"]')).perform()
#time.sleep(2)

#Mouse Hover
act.move_to_element(driver.find_element_by_xpath('//span[contains(text(),"TUTORIAL")]')).perform()

#Closing Browser
time.sleep(5)