import tweepy
from models.streamming import TweetStreamListener
import argparse
from models.kafka import KProducer
from models.arguments import Arguments
from models.api import KafkaApi
import sys
import time


if __name__ == '__main__':
    players = Arguments(sys.argv[1:]).players
    api = KafkaApi('conf/config.cfg').getApi()
    players_streammings = {}
    producer = KProducer()

    for player in players:
        print(f'{player}: ')
        streamPlayerListener = TweetStreamListener(producer.submitJsonMsg, 'json_msg', key=player)
        players_streammings[player] = tweepy.Stream(auth = api.auth, listener=streamPlayerListener)
        players_streammings[player].filter(track=[player], is_async=True, languages=["pt"])

    time.sleep(5)

    for player in players:
        players_streammings[player].disconnect()
