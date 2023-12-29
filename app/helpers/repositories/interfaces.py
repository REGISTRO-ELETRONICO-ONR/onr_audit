from abc import ABC, abstractmethod


class GetRecordsInterface(ABC):

    @staticmethod
    @abstractmethod
    def get(initial_date, finish_date, document=None):
        pass


class GetLogsInterface(ABC):

    @staticmethod
    @abstractmethod
    def get(initial_date, finish_date):
        pass
