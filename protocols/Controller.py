from abc import ABC, abstractmethod
from typing import Any


class Controller(ABC):
    @abstractmethod
    def execute(self) -> Any:
        pass
