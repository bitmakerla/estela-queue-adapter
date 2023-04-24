import json
import logging

from kafka import KafkaProducer

from estela_queue_adapter.abc_producer import ProducerInterface
from estela_queue_adapter.utils import get_bootstrap_servers, json_serializer


class KafkaProducerAdapter(ProducerInterface):
    def __init__(self, listeners, port):
        self.listeners = listeners
        self.port = port
        self.producer = None

    def on_kafka_send_error(self, excp):
        logging.error(str(excp))

    def get_connection(self):
        if self.producer is not None:
            return True
        try:
            bootstrap_servers = get_bootstrap_servers(self.listeners, self.port)
            self.producer = KafkaProducer(
                bootstrap_servers=bootstrap_servers,
                value_serializer=lambda x: json.dumps(
                    x, default=json_serializer
                ).encode("utf-8"),
                api_version=(0, 10),
                acks=1,
                retries=1,
            )
        except Exception as ex:
            logging.error(str(ex))
            return False
        return True

    def send(self, topic, data):
        self.producer.send(topic, value=data).add_errback(self.on_kafka_send_error)

    def flush(self):
        self.producer.flush()

    def close(self):
        self.producer.close()
