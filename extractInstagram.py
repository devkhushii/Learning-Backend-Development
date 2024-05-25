import instaloader
import re
import pandas as pd
import time
import random
from fake_useragent import UserAgent



proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}
ua = UserAgent()
print(ua.firefox)
headers = {'User-Agent':str(ua.firefox)}
 
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
username="kumari._.ankita"
password="KRani@12@"
bot.login(user=username, passwd=password)
time.sleep(random.randint(1, 15))
# bot.load_session_from_file("kumari._.ankita")

searchitem = input('Enter the search keyword\n')

time.sleep(random.randint(1, 15))
 # Provide the search query here
search_results = instaloader.TopSearchResults(bot.context, searchitem)
time.sleep(random.randint(1, 15))
# Iterating over the extracted usernames
for username in search_results.get_profiles():
    print(username)
# Iterating over the extracted hashtags
for hashtag in search_results.get_hashtags():
    print(hashtag)

 
target=input("enter userid of person whom details you want to extract:")
time.sleep(random.randint(1, 15))
# target="shubmangill"
# Loading the profile from an Instagram handle
profile = instaloader.Profile.from_username(bot.context, target)
time.sleep(random.randint(1, 15))
print(profile)
time.sleep(random.randint(1, 15))
print("Username: ", profile.username)
print("User ID: ", profile.userid)
print("Number of Posts: ", profile.mediacount)
print("Followers Count: ", profile.followers)
print("Following Count: ", profile.followees)
print("Bio: ", profile.biography)
print("External URL: ", profile.external_url)
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
print("Emails extracted from the bio:")
print(emails)
time.sleep(random.randint(1, 15))


# Retrieving the usernames of all followers
followers = [follower.username for follower in profile.get_followers()]
time.sleep(random.randint(1, 15))
# Converting the data to a DataFrame
followers_df = pd.DataFrame(followers)
 
# Storing the results in a CSV file
followers_df.to_csv('followers.csv', index=False)
 
# Retrieving the usernames of all followings
followings = [followee.username for followee in profile.get_followees()]
time.sleep(random.randint(1, 15))
# Converting the data to a DataFrame
followings_df = pd.DataFrame(followings)
 
# Storing the results in a CSV file
followings_df.to_csv('followings.csv', index=False)

time.sleep(random.randint(1, 15))
# Retrieving all posts in an object
posts = profile.get_posts()
time.sleep(random.randint(1, 15)) 
# Iterating and downloading all the individual posts
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")