

from typing import Dict, Union
import requests
from protocols.CurrencyConverter import CurrencyConverter


class RemoteCurrencyConverter(CurrencyConverter):
    def __init__(self, api_url: str, api_key: str, currency_country: str) -> None:
        self.api_url = api_url
        self.api_key = {'apikey': api_key}
        self.currency_country = currency_country

    def convertToDolar(self, amount: float) -> float:
        result = self.requestConvert(amount, 'USD')
        return result

    def convertToEuro(self, amount: float) -> float:
        result = self.requestConvert(amount, 'EUR')
        return result

    def _createParameters(self, amount: float, to: str) -> Dict[str, Union[int, str, float]]:
        params: Dict[str, Union[int, str, float]] = {
            'amount': amount,
            'from': self.currency_country,
            'to': to
        }
        return params

    def requestConvert(self, amount, to) -> float:
        response = requests.get(url=self.api_url,
                                data=None,
                                params=self._createParameters(amount, to),
                                headers=self.api_key)
        return response.json()['result']
