from abc import ABCMeta, abstractmethod


class ConsumerInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def __iter__(self):
        pass
