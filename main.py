from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get('https://web.skype.com/')

sleep(2)
email_element = driver.find_element_by_id('i0116')
email_element.send_keys("username")

sleep(2)
driver.find_element_by_id('idSIButton9').click()

sleep(2)
pass_element = driver.find_element_by_id('i0118')
pass_element.send_keys("pass")

sleep(1)
driver.find_element_by_id('idSIButton9').click()


