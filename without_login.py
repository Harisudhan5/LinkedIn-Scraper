from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() 

# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_argument("--incognito")
# Add arguments for IP rotation
#options.add_argument(f"--proxy-server={random_proxy()}") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 

driver = webdriver.Chrome(options = options)

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/in/athwal/')
time.sleep(5)

close_button_xpath = '//*[@id="base-contextual-sign-in-modal"]/div/section/button/icon'

# Wait for the element to be present and clickable
close_button = driver.find_element(By.XPATH,close_button_xpath)
close_button.click()

time.sleep(1)

try:
    user_name_xpath = '//*[@id="main-content"]/section[1]/div/section/section[1]/div/div[2]/div[1]/button/h1'
    user_name = driver.find_element(By.XPATH,user_name_xpath)
    user_name = str(user_name.get_attribute("innerHTML")).strip()
except Exception as e:
    user_name = str(e)

try:
    location_xpath = '//*[@id="main-content"]/section[1]/div/section/section[1]/div/div[2]/div[1]/h3/div/div[1]/span[1]'
    location = driver.find_element(By.XPATH,location_xpath)
    location = str(location.text).strip()
except Exception as e:
    location = str(e)

try:
    headline_xpath = '//*[@id="main-content"]/section[1]/div/section/section[1]/div/div[2]/div[1]/h2'
    headline = driver.find_element(By.XPATH,headline_xpath)
    headline = str(headline.text).strip()
except Exception as e:
    headline = str(e)

try:
    about_xpath = '//*[@id="main-content"]/section[1]/div/section/section[2]/div/p'
    about = driver.find_element(By.XPATH,about_xpath)
    about = str(about.text).strip()
except Exception as e:
    about = str(e)

print("User Name : ", user_name)
print("Location : ", location)
print("Headline : ", headline)
print("About : ",about)

