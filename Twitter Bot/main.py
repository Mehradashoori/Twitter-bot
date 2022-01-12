import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 16
PROMISED_UP = 8
CHROME_DRIVER_PATH = Service("/Users/USER/Desktop/Web Development/Chromedriver/chromedriver.exe")
TWITTER_EMAIL = "rc919295@gmail.com"
TWIITER_PASSWORD = "mehrad82"


class InternetSpeedTwiiterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        url = "https://speedtest.net/"
        self.driver.get(url)
        time.sleep(3)
        go_btn = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_btn.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text


    def tweet_at_provider(self):
        url = "https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJsYW5nIjoiZW4ifQ%3D%3D%22%7D"
        self.driver.get(url)
        time.sleep(3)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        next_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]')
        next_btn.click()
        username = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys("immhrd")

bot = InternetSpeedTwiiterBot(CHROME_DRIVER_PATH)
# bot.get_internet_speed()
bot.tweet_at_provider()
