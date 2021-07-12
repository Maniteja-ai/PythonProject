import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException


CHROME_DRIVER_PATH = "C:/Users/manit/OneDrive/Desktop/web development/CHROME/chromedriver_win32/" \
                     "chromedriver.exe"

INSTAGRAM_USER = INSTAGRAM_USERNAME
INSTAGRAM_PASS = PASSWORD
ACCOUNT = ACCOUNT WHOSE FOLLOWERS YOU NEED TO FOLLOW

class InstaFollowers:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get(' https://www.instagram.com/accounts/login/')
    def login(self):
        time.sleep(2)
        username = self.driver.find_element_by_name("username")
        username.send_keys(INSTAGRAM_USER)
        password = self.driver.find_element_by_name("password")
        password.send_keys(INSTAGRAM_PASS)
        time.sleep(4)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f'https://www.instagram.com/{ACCOUNT}/')
        self.followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        self.followers.click()
        time.sleep(2)
        element_inside_popup = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element_inside_popup)
            time.sleep(2)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector("li div div button")
        for follow_button in follow_buttons:
            try:
                follow_button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()
            finally:
                time.sleep(2)


instafollowers = InstaFollowers()
instafollowers.login()
instafollowers.find_followers()
instafollowers.follow()