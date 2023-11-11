import os
from typing import Generator, TextIO

import pytest


def get_first_char_from_lines(fp: TextIO) -> list[str]:
    "Retrieve the first character from each line in a file."
    return [line[0] for line in fp]


@pytest.fixture(scope="module")
def tmp_fp() -> Generator[TextIO, None, None]:
    "Return a file pointer"
    tmp_path = "tmp.txt"
    with open(tmp_path, "w+") as f:
        lines = [
            "This is the first line",
            "Now this is the second line",
            "And finally, the third line",
        ]
        f.writelines("\n".join(lines))
        f.seek(0)
        yield f
    os.remove(tmp_path)


def test_get_first_char_from_lines(tmp_fp: TextIO) -> None:
    assert get_first_char_from_lines(tmp_fp) == ["T", "N", "A"]
