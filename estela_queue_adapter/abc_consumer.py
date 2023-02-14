from abc import ABCMeta, abstractmethod


class ConsumerInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def consume(self):
        pass
