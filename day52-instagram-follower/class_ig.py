from tkinter import Scrollbar
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "new.chaoci@gmail.com"
PASSWORD = "post8430"
url = f"https://www.instagram.com/{SIMILAR_ACCOUNT}"

class InstaFollower:
    
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
    def login(self):
        self.driver.get(url)
        time.sleep(10)
        # login = self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_wi"]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/div[1]/a/button/div')
        # login.click()
        
        # time.sleep(5)
        
        user = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        user.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        
        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
        login_button.click()
        
        time.sleep(10)
        try:
            not_now = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
        
            not_now.click()
            
        except:
            print("NoSuchElementException")

    def find_followers(self):
        follower = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        follower.click()
        time.sleep(5)
        
        try:
            popup = self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        except:
            print("NoSuchElementException")
            
        try:
            for i in range(10):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)
                time.sleep(2)
        except:
            print("something wrong")

    def follow(self):
        try:
            followers = self.driver.find_elements(By.TAG_NAME,'button')
        except:
            print("NoSuchElementException")
        
        for x in followers[5:]:
            try:
                x.click()
                time.sleep(1)
            except:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()
    
bot = InstaFollower()
bot.login()
time.sleep(5)
bot.find_followers()
time.sleep(5)
bot.follow()