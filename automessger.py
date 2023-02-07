#Tinder bot that automatically messages any matches 


from selenium import webdriver 
from time import sleep 
from selenium.webdriver.common.keys import Keys

from Tinderlogin import email, password   

import openai

openaikey = 'Your API key here'

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
        
        

    

    def get_matches(self):
        match_profiles = self.driver.find_elements('class name', 'matchListItem')
        print(match_profiles)
        message_links = []
        for profile in match_profiles:
            if profile.get_attribute('href') == 'https://tinder.com/app/my-likes' or profile.get_attribute('href') == 'https://tinder.com/app/likes-you':
                continue
            message_links.append(profile.get_attribute('href'))
        return message_links

    def send_messages_to_matches(self):
        links = self.get_matches()
        for link in links:
            self.send_message(link)
            

    def send_message(self, link):
        self.driver.get(link)
        sleep(7)
        text_area = self.driver.find_element('xpath', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div[1]/div/div/div[3]/form/textarea')
        openai.api_key = openaikey

        # Set the model and prompt
        model_engine = "text-davinci-003"
        prompt = "I just matched with a girl on tinder. Give me a funny and confident pick up line without quotation marks"

        # Set the maximum number of tokens to generate in the response
        max_tokens = 1024

        # Generate a response
        completion = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.5,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

# Print the response


        text_area.send_keys(completion.choices[0].text)

        text_area.send_keys(Keys.ENTER)


bot = TinderBot()
bot.open_tinder()
sleep(5)
bot.send_messages_to_matches()


