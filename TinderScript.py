from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

class Tinderbot():
    def __int__(self):
        self.driver = webdriver.Chrome(r"C:\Users\16156\PycharmProjects\AutomatingStuff\tinder\chromedriver.exe")

    def login(self):
        self.driver.get('https://tinder.com')
        facebookusername = ""
        facebookpassword = ""

        sign_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button')
        sign_btn.click()
        fbt_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/span/div[2]/button')
        fbt_btn.click()

        # Focusing on Facebook popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])
        # End on focusing on Facebook
        email_ = self.driver.find_element_by_id('email')

        email_.send_keys(facebookusername)

        password_ = self.driver.find_element_by_id('pass')

        password_.send_keys(facebookpassword)
        password_.send_keys(Keys.RETURN)

       # fblogin_btn = self.driver.find_element_by_xpath('/html/body/div/div/form/div[2]/div/div[2]/div[1]/div[1]/button')
       # fblogin_btn.click()

        self.driver.switch_to.window(base_window)
        # Two pop-ups to exit out before entering Tinder program



        allow_btn = WebDriverWait(self.driver, 10).until(lambda driver: driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]'))
        allow_btn.click()
        not_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        not_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def auto_swipe(self):
        while True:
            time.sleep(0.6)
            try:
                self.like()
            except Exception:
                try:
                    self.close_match()
                except Exception:
                    self.close_pop_up()
    def close_match(self):
        pop_up = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/a')
        pop_up.click()
    def close_pop_up(self):
        pop_up = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
        pop_up.click()
