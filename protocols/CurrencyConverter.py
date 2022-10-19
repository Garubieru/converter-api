from abc import ABC, abstractmethod


class CurrencyConverter(ABC):
    @abstractmethod
    def convertToDolar(self):
        pass

    @abstractmethod
    def convertToEuro(self):
        pass
