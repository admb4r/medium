import random
from typing import Any

import pytest


def bubble_sort(arr: list[int]) -> list[int]:
    "A demo bubble sort."
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


@pytest.fixture(scope="module")
def random_and_sorted_list(request: Any) -> tuple[list, list]:
    "Return a randomised list of ints and a sorted version."
    # Extract out the argument passed from the test.
    n = request.param
    # Sanity check that we were passed what we were expecting.
    assert isinstance(n, int)
    # Create a list of the length requested.
    sorted_list = list(range(n))
    # Shuffle the list with a seed so it's repeatable.
    random_list = sorted_list.copy()
    random.Random(1).shuffle(random_list)
    # Return both the random list and the sorted list for comparison.
    return random_list, sorted_list


@pytest.mark.parametrize("random_and_sorted_list", [i for i in range(0, 110, 10)], indirect=True)
def test_bubble_sort(random_and_sorted_list: tuple[list, list]) -> None:
    # Unpack the two lists for readability.
    randomised_list, sorted_list = random_and_sorted_list
    assert bubble_sort(randomised_list) == sorted_list
