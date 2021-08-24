import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_exe_path = "/Users/nischalnairiti/Documents/InterviewPreparation/pythonProject/Angela100DaysOfCodePython/selenium/development/chromedriver"
driver = webdriver.Chrome(executable_path=driver_exe_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

big_cookie = driver.find_element_by_id("bigCookie")

game_start = time.time()
click_start = game_start
while True:
    big_cookie.click()
    click_end = time.time()  
        
    if click_end-click_start >= 5:
        product_enabled = driver.find_elements_by_css_selector("#products .enabled")
        highest_price = 0
        try:
            for product in product_enabled:
                # print(product.text)
                product_price = product.text.split('\n')[1].replace(',','')
                product_price = int(product_price)
        except IndexError:
            print('Out of range')
        else:
            if product_price > highest_price:
                highest_price = product_price
                highest_product = product
                cookies = driver.find_element_by_id("cookies")
                cookies_collected = cookies.text.split('\n')[0].split()[0].replace(',','')
                cookies_collected = int(cookies_collected)
                if cookies_collected >= highest_price:
                    highest_product.click()
        finally:
            click_start = click_end
    if click_end-game_start >= 300:
        cookie_per_second = driver.find_element_by_css_selector("#cookies div").text
        print('Cookie',cookie_per_second)
        break

# driver.quit()
