#https://www.youtube.com/watch?v=nveXi3bkeZs&list=PLIMhDiITmNrLuNNLkHRvNS9ivyVCzj2oA

import time

#Opera Browser-setup
from selenium import webdriver
from selenium.webdriver.chrome import service
webdriver_service = service.Service('F:\\SELENIUM\\operadriver_win64\\operadriver.exe')
webdriver_service.start()
driver = webdriver.Remote(webdriver_service.service_url)
driver.get("http://www.thetestingworld.com/testings/")

#Maximizing the Window
driver.maximize_window()

#Working on Text-Boxes
driver.find_element_by_name('fld_username').send_keys('Hello World')
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys('qwerty@123')
driver.find_element_by_name('fld_password').send_keys('qwerty')
driver.find_element_by_name('fld_cpassword').send_keys('qwerty')
driver.find_element_by_name('fld_username').clear()
driver.find_element_by_name('fld_username').send_keys('qwerty')

#Working on Radio-Button
driver.find_element_by_xpath('//input[@value="home"]').click()

#Working on Check-Boxes
driver.find_element_by_xpath('//input[@name="terms"]').click()
 
#Working on Drop-Down
from selenium.webdriver.support.select import Select
obj = Select(driver.find_element_by_name('sex'))
obj.select_by_index(1)

# Working on Buttons
#driver.find_element_by_xpath('//input[@value="Sign up"]').click()

#Working on Links
driver.find_element_by_class_name('displayPopup').click()
time.sleep(2)
driver.find_element_by_class_name('close').click()

#Closing Browser
time.sleep(2)
driver.close()