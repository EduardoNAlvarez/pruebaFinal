import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("chromedriver.exe")	
driver.get("http://192.168.56.102:8106/")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")
elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("password")
elemento2.send_keys(Keys.ENTER)
driver.get("http://192.168.56.102:8106/")
elemento3 = driver.find_element(By.ID, "CreateTicketInQueue")
elemento3.click()
elemento4 = driver.find_element(By.NAME, "Subject")
elemento4.send_keys("Es un asunto importante")
elemento5 = driver.find_element(By.NAME, "SubmitTicket")
elemento5.click()

time.sleep(20)
driver.close()