from base_formatter import BaseFormatter


class HexFormatter(BaseFormatter):
    "A formatter that converts its input to hex."

    def format(self, data: str) -> str:
        return data.encode("utf-8").hex()
