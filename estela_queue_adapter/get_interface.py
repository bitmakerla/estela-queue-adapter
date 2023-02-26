import os

from estela_queue_adapter.kafka.consumer import KafkaConsumerAdapter
from estela_queue_adapter.kafka.producer import KafkaProducerAdapter


producer_interfaces = {"kafka": KafkaProducerAdapter}
consumer_interfaces = {"kafka": KafkaConsumerAdapter}


def parse_queue_params():
    prefix = "QUEUE_PLATFORM_"
    env_vars = [var for var in os.environ if var.startswith(prefix)]
    params = {var[len(prefix) :].lower(): os.environ[var] for var in env_vars}
    return params


def get_interface(interfaces):
    platform, args = os.getenv("QUEUE_PLATFORM"), parse_queue_params()
    if platform not in interfaces:
        raise Exception(
            f"The queuing platform '{platform}' is not currently supported."
        )
    return interfaces[platform](**args)


def get_producer_interface():
    return get_interface(producer_interfaces)


def get_consumer_interface():
    return get_interface(consumer_interfaces)
