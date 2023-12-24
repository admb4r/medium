from abc import ABC, abstractmethod


class BaseFormatter(ABC):
    "Defines an interface for all formatters."

    @abstractmethod
    def format(self, data: str) -> str:
        raise NotImplementedError
