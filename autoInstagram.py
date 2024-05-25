
import pandas as pd
import time
import random
from fake_useragent import UserAgent
from instabot import Bot


proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}
ua = UserAgent()
print(ua.chrome)
headers = {'User-Agent':str(ua.chrome)}

bot=Bot()

username="khushi.__.rani16"
password="KRani@12@"
bot.login(username=username, password=password)
time.sleep(random.randint(1, 15))

bot.upload_photo("fire2.jpg", caption="symbol of sprituality")