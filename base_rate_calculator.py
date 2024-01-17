from abc import ABC, abstractmethod


class BaseRateCalculator(ABC):
    """ This is a Interface Step """
    
    @abstractmethod
    def insert_prefix_rate(self, prefix: str, rate: float):
        raise NotImplemented('Not Implemented yet')
    
    @abstractmethod
    def get_rate_for_number(self, number: str):
        raise NotImplemented('Not Implemented yet')