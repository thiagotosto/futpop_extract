import tweepy
import json

class TweetStreamListener(tweepy.StreamListener):

    def __init__(self, handler, data_arg, **kwargs):
        tweepy.StreamListener.__init__(self)
        self.handler = handler
        self.kwargs = kwargs
        self.data_arg = data_arg

    def on_data(self, data):
        try:
            tweet = data
            if 'retweeted_status' not in json.loads(tweet).keys():
                print(json.loads(tweet))
                self.kwargs[self.data_arg] = data
                self.handler(**self.kwargs)
        except Exception as e:
            print(e)
