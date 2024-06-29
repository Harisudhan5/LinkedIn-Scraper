from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import random 
import config

def random_proxy():
    proxy = random.choice(config.ips)
    return proxy 


options = webdriver.ChromeOptions() 
 
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 

# Add arguments for IP rotation
options.add_argument(f"--proxy-server={random_proxy()}") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 

driver = webdriver.Chrome(options = options)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login/')
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys('harisudhans574@gmail.com')
time.sleep(1.5)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('1@AiDataLearning')
time.sleep(1.5)
log_in_button = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
log_in_button.click()
#driver.get('https://whatismyipaddress.com/')
html = driver.page_source
soup = BeautifulSoup(html)
print(soup)
time.sleep(10)

