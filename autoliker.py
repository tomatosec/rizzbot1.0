#Tinder bot that swipes right 70% of the time
from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.keys import Keys

from Tinderlogin import email, password   

import random



class TinderBot(): 
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open_tinder(self): 
        self.driver.get('https://tinder.com')

        sleep(2)
        login = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
        login.click()
        sleep(1)
        self.google_login()
        sleep(1)
        


        

    def google_login(self): 
        login_with_google = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
        login_with_google.click()

        sleep(2)
        base_window = self.driver.window_handles[0]
        google_popup_window = self.driver.window_handles[1]

        self.driver.switch_to.window(google_popup_window)

        #login to FB 

        email_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[1]/div/input')
        pw_field = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[2]/div/input')
        login_button = self.driver.find_element('xpath', '/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input')
        # enter email, password and login
        email_field.send_keys(email)
        pw_field.send_keys(password)
        login_button.click()
        self.driver.switch_to.window(base_window)

        #Should be logged in! 

        sleep(3)
        try:
            allow_location_button = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
            allow_location_button.click()
        except:
            print('no location popup')

        sleep(2)

        try:
            notifications_button = self.driver.find_element('xpath', '/html/body/div[2]/main/div/div/div/div[3]/button[1]')
            notifications_button.click()
        except:
            print('no notification popup')

        try: 
            cookies_deny = self.driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
            cookies_deny.click()
        except: 
            print('no notification popup')
        
        

    def right_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_RIGHT)
    def left_swipe(self):
        doc = self.driver.find_element('xpath', '//*[@id="Tinder"]/body')
        doc.send_keys(Keys.ARROW_LEFT)


    #like 70% of the time
    def auto_swipe(self):
         

        for i in range(50):  
            random_number = random.uniform(0, 1)
            if random_number < 0.7:
                sleep(2)
                try:
                    self.right_swipe()
                except:
                    self.close_match()
            else:
                self.left_swipe() 


    def close_match(self):
        match_popup = self.driver.find_element('xpath', '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.open_tinder()
sleep(5)
bot.auto_swipe()
