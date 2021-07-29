from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
import time
from passwords import email, password
 
options.Options.add_argument("--disable-web-security")
options.Options.add_argument("--user-data-dir=true")
options.Options.add_argument("--allow-running-insecure-content") 

driver = webdriver.Chrome(executable_path="venv/bin/chromedriver")


driver.maximize_window()
driver.get('https://calendar.google.com/calendar/u/0/r/month?tab=rc')

# sign in
# element = driver.find_element_by_id("yDmH0d")
element = driver.find_element_by_xpath("//input[@id='identifierId']").send_keys(email)
driver.find_element_by_id("identifierNext").click()
   



     