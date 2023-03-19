import os

from estela_queue_adapter.kafka.consumer import KafkaConsumerAdapter
from estela_queue_adapter.kafka.producer import KafkaProducerAdapter


producer_interfaces = {"kafka": KafkaProducerAdapter}
consumer_interfaces = {"kafka": KafkaConsumerAdapter}


def get_queue_env_vars():
    prefix = "QUEUE_PLATFORM"
    env_vars = [var for var in os.environ if var.startswith(prefix)]
    result = {var: os.environ[var] for var in env_vars}
    return result


def parse_queue_args():
    prefix = "QUEUE_PLATFORM_"
    env_vars = [var for var in os.environ if var.startswith(prefix)]
    args = {var[len(prefix) :].lower(): os.environ[var] for var in env_vars}
    return args


def get_interface(interfaces, **args):
    platform, env_args = os.getenv("QUEUE_PLATFORM"), parse_queue_args()
    if platform not in interfaces:
        raise Exception(
            f"The queuing platform '{platform}' is not currently supported."
        )
    env_args.update(args)
    return interfaces[platform](**env_args)


def get_producer_interface(**args):
    return get_interface(producer_interfaces, **args)


def get_consumer_interface(**args):
    return get_interface(consumer_interfaces, **args)
