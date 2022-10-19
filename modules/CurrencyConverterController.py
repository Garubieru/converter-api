from typing import Any
from protocols.Controller import Controller
from protocols.CurrencyConverter import CurrencyConverter


class CurrencyConverterController(Controller):
    def __init__(self, currency_converter: CurrencyConverter) -> None:
        self.currency_converter = currency_converter

    def execute(self, amount: str) -> Any:
        parsed_amount = float(amount)
        return {
            'conversao': {
                'real': parsed_amount,
                'dolar': self.currency_converter.convertToDolar(parsed_amount),
                'euro': self.currency_converter.convertToEuro(parsed_amount),
            }
        }
