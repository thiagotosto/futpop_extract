from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

class KProducer():
    def __init__(self):
        pass

    def _on_send_success(self):
        print(record_metadata.topic)
        print(record_metadata.partition)
        print(record_metadata.offset)

    def _on_send_error(self):
        log.error('I am an errback', exc_info=excp)

    def submitJsonMsg(self, key, json_msg):
        producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'),
                                 retries=5)

        producer.send('json-topic', {'msg': json_msg}, key=str.encode(key))\
                .add_callback(self._on_send_success)\
                .add_errback(self._on_send_error)


    def flush(self, producer):
        producer.flush()
