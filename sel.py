# need instal these packets
# pip install selenium
# pip install time
# end
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import configparser
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

cnfg = config['parameters']

driver = webdriver.Chrome(cnfg['chromedriver_url'])
driver.get(cnfg['login_url'])

#element_login  = driver.find_element(By.XPATH,'//input[@type="email"]')
element_login  = driver.find_element(By.XPATH,"//div[contains(@class,'form-control_type_email')]//input")

#element_login.send_keys('mgolovin@incap-dev.ru')
element_login.send_keys(cnfg['login'])
element_pass  = driver.find_element(By.XPATH,'//input[@type="password"]')
element_pass.send_keys(cnfg['password'])
element_accept = driver.find_element(By.XPATH,'//div[@class="cookie-agreement"]/div[1]/div[2]/button')
element_accept.click()
element_login  = driver.find_element(By.XPATH,'//div[@id="app"]/div[1]/button[1]/div[1]')
element_login.click()
time.sleep(5)
driver.get(cnfg['final_chrono_url'])

while True:
    #element_refresh = driver.find_element(By.XPATH,'//div[@class="body-content"]/div[1]/div[2]/div[6]/div[1]/div[3]/button')
    element_refresh = driver.find_element(By.XPATH,'//div[@class="body-content"]/div[1]/div[2]/div[not(contains(@style,"display: none"))]/div[1]/div[3]/button')
    #element_refresh = driver.find_element(By.XPATH,'//div[@class="body-content"]/div[1]/div[2]/div[15]/div[1]/div[3]/button')
    element_refresh.click()
    print(time.ctime())
    time.sleep(600)
