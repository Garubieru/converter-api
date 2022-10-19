from factories.RemoteCurrencyConverterFactory import create_remote_currency_converter
from modules.CurrencyConverterController import CurrencyConverterController
from modules.Server import Server
from dotenv import dotenv_values

config = dotenv_values()

if __name__ == "__main__":
    server = Server()
    server.add_route('/convertemoeda/<amount>',
                     'convertemoeda', CurrencyConverterController(create_remote_currency_converter()))
    server.listen(config['PORT'], config['HOST'])
