from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

class KProducer():
    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers

    def _on_send_success(self):
        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)

    def _on_send_error(self):
        log.error('I am an errback', exc_info=excp)

    def submitJsonMsg(self, key, json_msg):
        producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                 value_serializer=lambda m: json.dumps(m).encode('ascii'),
                                 retries=5,
                                 #security_protocol="PLAINTEXT"
                                 )

        producer.send('tweet_to_classify', {'msg': json_msg}, key=str.encode(key))\
                .add_callback(self._on_send_success)\
                .add_errback(self._on_send_error)


    def flush(self, producer):
        producer.flush()
