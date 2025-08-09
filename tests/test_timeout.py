import time

from niobium.timeout import ImplicitWait


def test_implicit_wait_max_time_exceeded():
    ImplicitWait.time_to_wait = 1
    implicit_wait = ImplicitWait()
    implicit_wait.start()
    assert not implicit_wait.max_time_exceeded
    time.sleep(1)
    assert implicit_wait.max_time_exceeded
