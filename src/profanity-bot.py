import argparse
import json
import requests
import schedule
import sys
import time
import tweepy

class Profanity():
    def __init__(self):
        api_key             = ""
        api_secret          = ""
        access_token        = ""
        access_token_secret = ""

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        self.get_args()

    def get_bad_word(self):
        response = requests.get("https://insult.mattbas.org/api/insult")
        return response.text

    def get_args(self):
        parser = argparse.ArgumentParser(description="Twitter Profanity Bot")
        parser.add_argument("-m", action="store", dest="minutes", required=True, help="Bot runs everys X minutes")
        parser.add_argument("-t", action="store", dest="target", required=True, help="Target user(s)")
        self.arguments = parser.parse_args()

    def get_minutes(self):
        return int(self.arguments.minutes)

    def get_target(self):
        return self.arguments.target

    def get_tweet(self, users):
        bad_word = self.get_bad_word()
        return users + " " + bad_word

    def verify_tweet_size(self, tweet):
        return False if len(tweet) > 280 else True

    def offend(self):
        users = self.get_target()
        tweet = self.get_tweet(users)
        print(tweet)
        if self.verify_tweet_size(tweet) is True:
            self.api.update_status(status=tweet)

def main():
    res = Profanity()
    minutes = res.get_minutes()
    schedule.every(minutes).minutes.do(res.offend)

    while True:
       schedule.run_pending()
       time.sleep(1)

if __name__ == "__main__":
    main()
