import json
import logging

from kafka import KafkaConsumer

from estela_queue_adapter.abc_consumer import ConsumerInterface
from estela_queue_adapter.utils import get_bootstrap_servers


class KafkaConsumerAdapter(ConsumerInterface):
    def __init__(self, listeners, port, topic, queue_max_timeout):
        self.listeners = listeners
        self.port = port
        self.topic = topic
        self.queue_max_timeout = queue_max_timeout
        self.consumer = None

    def get_connection(self):
        if self.consumer is not None:
            return True
        try:
            max_poll_interval_ms = self.queue_max_timeout * 1500
            bootstrap_servers = get_bootstrap_servers(self.listeners, self.port)
            _consumer = KafkaConsumer(
                self.topic,
                bootstrap_servers=bootstrap_servers,
                auto_offset_reset="earliest",
                enable_auto_commit=True,
                auto_commit_interval_ms=1000,
                group_id="group_{}".format(self.topic),
                api_version=(0, 10),
                value_deserializer=lambda x: json.loads(x.decode("utf-8")),
                max_poll_interval_ms=max_poll_interval_ms,
                session_timeout_ms=max_poll_interval_ms,
                request_timeout_ms=max_poll_interval_ms + 1,
                connections_max_idle_ms=max_poll_interval_ms + 2,
            )
        except Exception as ex:
            logging.error(str(ex))
            return False
        return True
