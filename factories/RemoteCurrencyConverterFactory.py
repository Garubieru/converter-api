from modules.RemoteCurrencyConverter import RemoteCurrencyConverter


def create_remote_currency_converter() -> RemoteCurrencyConverter:
    return RemoteCurrencyConverter(
        api_url='https://api.apilayer.com/exchangerates_data/convert',
        api_key='SnPyLmJ0v0nbofm96Ko0fb6VkNwdCWE0',
        currency_country='BRL')
