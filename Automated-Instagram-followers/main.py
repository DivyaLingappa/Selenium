# Automate instagram login. Get the account of interest(homecookingshow), go to the followers and follow
# certain number of people
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException

class InstagramFollow:
    def __init__(self,path):
        self.path = path
    def login(self):
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.driver.get("https://www.instagram.com")
        sleep(2)
        email = self.driver.find_element_by_name("username")
        email.send_keys("xyz@gmail.com")
        sleep(2)
        password = self.driver.find_element_by_name("password")
        password.send_keys("123456")
        sleep(2)
        log_in = self.driver.find_element_by_xpath('//div[text()="Log In"]') 
        log_in.click()
        sleep(5)
        info_save_disable = self.driver.find_element_by_xpath('//button[text()="Not Now"]')
        info_save_disable.click()
        sleep(2)
        notification_disable = self.driver.find_element_by_xpath('//button[text()="Not Now"]')
        notification_disable.click()
        sleep(2)
    def find_followers(self,profile_name):
        self.driver.get(f"https://www.instagram.com/{profile_name}")
        sleep(3)
#         search = self.driver.find_element_by_xpath('//input[@placeholder="Search"]') 
#         search.send_keys(profile_name)
#         sleep(2)
#         search.send_keys(Keys.ENTER)
        followers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        sleep(3)
#         modal = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        modal = self.driver.find_element_by_class_name("isgrP")
        sleep(3)
        for i in range(3): # scroll down three times
            self.follow_people()
            sleep(5)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
    def follow_people(self):
        follow_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in follow_buttons:
            try:
                sleep(2)
                button.click()
            except ElementClickInterceptedException:
                sleep(1)
                cancel_button = self.driver.find_element_by_xpath('//button[text()="Cancel"]')
                cancel_button.click()
                
#        self.driver.quit()
        
                
driver_exe_path = "../development/chromedriver"
bot = InstagramFollow(driver_exe_path)
bot.login()
bot.find_followers("homecookingshow")
