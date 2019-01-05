import json


from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key = 'DbqG9FSwS4aw9AJ3eI0L85POh'
consumer_secret = 'ciZzYDvFtY1cT3lzIguMYP4E4DAPkScJWImm2bPeWpTSTpToxf'
access_token = '932365085611319302-UPrqZvTfu3V8eVbNeWaXjRC8s9pkszu'
access_token_secret = 'BMPG8U4s5aEsDvPOsoZYGqPDNHur264jTw2AauhFdqRs9'

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name, status.created_at, status.source, '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True # keep stream alive

    def on_timeout(self):
        print('Listener timed out!')
        return True

def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)

def pull_down_tweets(screen_name):
    api = API(auth)
    # if the authentication was successful, you should see the name of the
    # account
    # print(api.me().name)
    # if the application settings are set for "Read and Write" then this line
    # should tweet out the message to your account's timeline.
    # api.update_status(status='Updating using OAuth authentication via Tweepy!')
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))


if __name__ == '__main__':
    # print_to_terminal()
    pull_down_tweets(auth.username)

