
from flask import Flask
from protocols.Controller import Controller


class Server:
    def __init__(self) -> None:
        self.app: Flask = Flask(__name__)

    def listen(self, port: int):
        self.port = port
        self.app.run(port=port)

    def add_route(self, endpoint: str, endpoint_name: str, controller: Controller):
        self.app.add_url_rule(
            endpoint, endpoint_name, controller.execute)
