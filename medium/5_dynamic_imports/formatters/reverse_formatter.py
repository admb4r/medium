from base_formatter import BaseFormatter


class ReverseFormatter(BaseFormatter):
    "A formatter that reverses its input."

    def format(self, data: str) -> str:
        return data[::-1]
