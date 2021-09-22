from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from passwords import email, password


# o = Options() 
# o.add_argument("--disable-web-security")
# o.add_argument("--user-data-dir=true")
# o.add_argument("--allow-running-insecure-content") 

driver = webdriver.Chrome('venv/bin/chromedriver')



driver.get('https://todoist.com/users/showlogin')

driver.maximize_window()
#sign in
time.sleep(1)
driver.find_element_by_xpath("//input[@id='email']").send_keys(email)

time.sleep(1)
driver.find_element_by_name('password').send_keys(password)

time.sleep(1)
driver.find_element_by_class_name('submit_btn.ist_button.ist_button_red.sel_login').click()

#add workout
time.sleep(1)
driver.find_element_by_class_name("plus_add_button").click()

time.sleep(1)
driver.find_element_by_css_selector('div.public-DraftStyleDefault-block.public-DraftStyleDefault-ltr').send_keys('Workout')


time.sleep(1)
driver.find_element_by_css_selector('textarea.task_editor__description_field.no-focus-marker').send_keys('Workout')
#change date
time.sleep(1)
driver.find_element_by_css_selector('button.item_due_selector.icon_pill').click()

time.sleep(1)
element = driver.find_element_by_css_selector('span.date.date_today')
driver.execute_script("arguments[0].setAttribute('class','date')", element)

time.sleep(1)
driver.execute_script("""document.querySelector("span[class='date']").value="Sep 30";""")
print(666)
time.sleep(1)
driver.find_element_by_css_selector('button.reactist_button.reactist_button--primary').click()

