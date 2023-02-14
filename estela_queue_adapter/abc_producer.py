from abc import ABCMeta, abstractmethod


class ProducerInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def flush(self):
        pass

    @abstractmethod
    def close(self):
        pass
