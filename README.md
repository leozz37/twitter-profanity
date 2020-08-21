# A Twitter Bot to Offend Target Users

Send offenses to a target user(s) on Twitter every pre determinate minutes. 

You need to enable Twitter Dev Account to your account to use this bot. You can enable yours at https://apps.twitter.com/, is pretty easy and fast. Create an App and generate API and Consumer tokens.

![teste](https://i.ibb.co/zxTKWPv/twitter-tokens.png)

Place them on `profanity-bot.py` parameters:

```
api_key             = ""
api_secret          = ""
access_token        = ""
access_token_secret = ""
```


## Installing

Clone this repository:

`$ git clone https://github.com/leozz37/twitter-profanity-bot.git`

Install the dependencies:

`$ pip install -r requirements.txt`

## Parameters

There's two required parameters:
```
-t:     Target users, "@realDonaldTrump" or for multiple users:
        "@realDonaldTrump @leozzils".
-m:     Minutes, the bot will tweet every X minutes.
```

## Running

`$ python src/profanity-bot.py -m 15 -t "@realDonaldTrump @leozzils"`
