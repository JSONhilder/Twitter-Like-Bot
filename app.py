import os 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Environment varables
t_user = os.environ.get('USER_N')
t_pass = os.environ.get('USER_P')

# print(t_user)
# print(t_pass)



class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #create an instance of bot
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        WebDriverWait(bot, 10).until( EC.presence_of_element_located((By.NAME, 'session[username_or_email]')))
        WebDriverWait(bot, 10).until( EC.presence_of_element_located((By.NAME, 'session[password]')))
        #inspect page to look for unique identifier of an element to find with bot.
        username = bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        #.clear() to make sure the entry fields are empty
        username.clear()
        password.clear()
        #to input the values inside the textbox/area we can use .send_keys() to pass the key
        #use parameters defined in the class
        username.send_keys(self.username)
        password.send_keys(self.password)
        #on twitter if you have typed your pass and in the text area you can use enter to log in, do that rather than click button.
        #with import Keys we can make use of the keys on the keyboard we can use enter as RETURN
        password.send_keys(Keys.RETURN)
        time.sleep(5)

    def search_tweet(self, hashtag):
            no_of_pagedowns = 10
            bot = self.bot
            #here we can search a url and determind what changes per search and replicate it with an f string, and passing the value/s that change
            bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
            WebDriverWait(bot, 10).until( EC.presence_of_element_located((By.TAG_NAME, 'body')))
            elem = bot.find_element_by_tag_name("body")
            while no_of_pagedowns:
                elem.send_keys(Keys.PAGE_DOWN)
                time.sleep(1.5)
                no_of_pagedowns-=1

    def like_tweets(self):
        bot = self.bot
        WebDriverWait(bot, 10).until( EC.presence_of_element_located((By.XPATH, "//div[@data-testid='tweet']")))
        #finds all divs with tweet and stores the element in a list.
        tweets = bot.find_elements_by_xpath("//div[@data-testid='tweet']")
        print(len(tweets))
        for tweet in tweets:
            #finds the div for the like button if a post has already been liked it will change the data-testid to unlike therefore this wont remove any previous likes if it finds the same tweet as before
            like = bot.find_element_by_xpath("//div[@data-testid='like']")
            like.click()
            likes  -= 1
            time.sleep(40)
            

like_bot = TwitterBot(t_user, t_pass) #use environment variables
like_bot.login()
like_bot.search_tweet('linux zsh')
like_bot.like_tweets()