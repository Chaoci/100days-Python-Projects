from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class InternetSpeedTwitterBot:
    
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down = 0
        self.up = 0
        
    def get_internet_speed(self):
        url = "https://www.speedtest.net/setting"

        self.driver.get(url)
        time.sleep(120)

        go_button = self.driver.find_element(By.CLASS_NAME, value="js-start-test")
        go_button.click()
        time.sleep(5)

        download_data = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        upload_data = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text

        print(f"down: {download_data}\nup: {upload_data}")
        
    def tweet_at_provider(self):
        if int(self.down) < 20 and int(self.up) < 15:
            print("GG")
        else:
            print("nice")