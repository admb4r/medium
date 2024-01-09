import json

from typeguard import typechecked


@typechecked
def foo(i: int) -> None:
    "Print a number..."
    print(i)


@typechecked
def bar(data: str) -> None:
    "Parse some JSON and print it..."
    d = json.loads(data)
    foo(d)


if __name__ == "__main__":
    bar('{"test": 123}')
