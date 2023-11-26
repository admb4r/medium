import time

import pytest


# With scope set to `session` the two tests will take ~5 seconds to run. The fixture will
# be created for the session and reused across both tests.
# Set the scope to `function` and watch the tests take twice as long as the fixture is
# created and destructed for each test.
@pytest.fixture(scope="session")
def time_consuming_fixture() -> int:
    "A fixture which takes a long time!"
    time.sleep(5)
    return 1


def test_time_consuming_fixture(time_consuming_fixture: int) -> None:
    assert time_consuming_fixture == 1


def test_time_consuming_fixture_again(time_consuming_fixture: int) -> None:
    assert time_consuming_fixture == 1
