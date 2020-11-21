import configparser
import tweepy

class KafkaApi():
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.config.read(file)
        self.credentials = self._getCredentials()

    def _getCredentials(self):
        return {k:v for k,v in self.config['credentials'].items()}

    def getApi(self):
        consumer_key = self.credentials['consumer_key']
        consumer_secret = self.credentials['consumer_secret']
        access_token = self.credentials['access_token']
        access_token_secret = self.credentials['access_token_secret']

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        return tweepy.API(auth)
