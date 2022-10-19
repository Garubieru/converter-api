from factories.RemoteCurrencyConverterFactory import create_remote_currency_converter
from modules.CurrencyConverterController import CurrencyConverterController
from modules.Server import Server

if __name__ == "__main__":
    server = Server()
    server.add_route('/convertemoeda/<amount>',
                     'convertemoeda', CurrencyConverterController(create_remote_currency_converter()))
    server.listen(5000)
