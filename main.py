# need instal these packets
# pip install selenium
# pip install time
# pip install webdriver-manager
# end
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import configparser
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

cnfg = config['parameters']

options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(cnfg['login_url'])

element_login  = driver.find_element(By.XPATH,"//div[contains(@class,'form-control_type_email')]//input")

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
    element_refresh = driver.find_element(By.XPATH,'//div[@class="body-content"]/div[1]/div[2]/div[not(contains(@style,"display: none"))]/div[1]/div[3]/button')
    element_refresh.click()
    print(time.ctime())
    time.sleep(60)
