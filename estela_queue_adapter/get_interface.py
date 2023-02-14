from estela_queue_adapter.kafka.producer import KafkaProducerAdapter

interfaces = {"kafka": KafkaProducerAdapter}


def get_producer_interface(platform, **args):
    if platform not in interfaces:
        raise Exception(
            f"The queuing platform '{platform}' is not currently supported."
        )
    return interfaces[platform](**args)
