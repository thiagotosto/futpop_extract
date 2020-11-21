import tweepy
import json

#autenticação twitter
consumer_key="jHM5NQ2laLIUvSftKY7ollzCR"
consumer_secret="EaMcEGRhweXaxGdGHiBCkQELJ3k2pRR8G6twANblgr7CJhcJun"
access_token="236888293-RAEsy7oTqFtEpUXzG0fn06ioaTjcG700OlYOxzZq"
access_token_secret="i0lSrUk0RAPUUMTKWjzrPG4uEtepqy37Y6pK95U5BwvNy"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class TweetStreamListener(tweepy.StreamListener):

    def __init__(self, file_path):
        tweepy.StreamListener.__init__(self)
        self.file_path = file_path

    def on_data(self, data):
        try:
            tweet = data

            if 'retweeted_status' not in json.loads(tweet).keys():
                print(json.loads(tweet))
                with open(self.file_path, 'a') as f:
                    f.write(tweet)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    streamPlayerListener = TweetStreamListener('files/tite.txt')
    streamPlayer = tweepy.Stream(auth = api.auth, listener=streamPlayerListener)
    streamPlayer.filter(track=['tite'], is_async=False, languages=["pt"])

    #streamPlayer.disconnect()
