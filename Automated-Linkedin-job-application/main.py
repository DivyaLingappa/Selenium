# Automate linkedin login. Search for jobs in preferred city and apply for 1st job using easy apply.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_exe_path = "../development/chromedriver"
driver = webdriver.Chrome(executable_path=driver_exe_path)

driver.get("https://linkedin.com")

email = driver.find_element_by_name("session_key")
password = driver.find_element_by_name("session_password")
sign_in = driver.find_element_by_class_name("sign-in-form__submit-button")

sleep(1)
email.send_keys("xyz@gmail.com")
sleep(1)
password.send_keys("123456")
sleep(1)
sign_in.click()
sleep(1)

search = driver.find_element_by_class_name("search-global-typeahead__input")
search.send_keys("Python Developer")
search.send_keys(Keys.ENTER)
sleep(3)
# Using a div for example: .driver.find_element_by_css_selector("div[aria-label='XXXX']")
job_button = driver.find_element_by_css_selector("[aria-label='Jobs']")
job_button.click()

sleep(3)

city_search = driver.find_element_by_css_selector("[aria-label='City, state, or zip code']")
city_search.clear()
# city_search.send_keys(Keys.COMMAND + "a")
# city_search.send_keys(Keys.DELETE)
city_search.send_keys("Mississauga")
city_search.send_keys(Keys.ENTER)

sleep(3)
job_titles = driver.find_elements_by_css_selector(".job-card-container--clickable .artdeco-entity-lockup__title a")
for job in job_titles:
    print(job.text)

# Apply for 1st job with easy apply
sleep(2)
easy_apply_check = driver.find_element_by_css_selector(".jobs-s-apply .jobs-apply-button span")
if easy_apply_check.text == "Easy Apply":
    easy_apply = driver.find_element_by_css_selector(".jobs-s-apply .jobs-apply-button")
    easy_apply.click()
    phone_number = driver.find_element_by_css_selector("input")
    phone_number.send_keys("12361273")
    next_button = driver.find_element_by_css_selector("[aria-label='Continue to next step']")
    next_button.click()
    sleep(2)
    next_button.click()
    close_button = driver.find_element_by_css_selector("[aria-label='Dismiss']")
    close_button.click()
    discard = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[3]/button[2]")
    discard.click()
    
driver.quit()
