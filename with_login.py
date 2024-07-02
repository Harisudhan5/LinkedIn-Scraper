from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import random 
import config
'''
harisudhans574@gmail.com
1@AiDataLearning
'''



options = webdriver.ChromeOptions() 
 
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 

# Add arguments for IP rotation
#options.add_argument(f"--proxy-server={random_proxy()}") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 

driver = webdriver.Chrome(options = options)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login/')
username = driver.find_element(By.XPATH, '//*[@id="username"]')
username.send_keys('nirmala.61280@gmail.com')
time.sleep(1.5)
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('1Linkedin@123')
time.sleep(1.5)
log_in_button = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')

log_in_button.click()

time.sleep(1)

driver.get('https://www.linkedin.com/in/athwal/')
time.sleep(3.5)

data = str(driver.page_source)

soup = BeautifulSoup(data,"html.parser")

name_tag = soup.find('h1',class_='text-heading-xlarge inline t-24 v-align-middle break-words').text
name = str(name_tag).strip()

headline_tag = soup.find('div',class_='text-body-medium break-words').text
headline = str(headline_tag).strip()

location_tag = soup.find('span',class_='text-body-small inline t-black--light break-words').text
location = str(location_tag).strip()

about_content = []

about_box = soup.find('div',class_='HMZyUxfpaKOqYknGYzBkgbOfYbcgWdYsLo full-width t-14 t-normal t-black display-flex align-items-center').div
about_tags = about_box.find_all('span') 
for content in about_tags:
    about_content.append(content)


print("Name = ", name)
print("Headline = ",headline)
print("Location = ",location)
print("About = ",about_content)


