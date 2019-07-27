# -*- coding: utf-8 -*-
import pytest

import niobium


def pytest_addoption(parser):
    parser.addoption(
        "--website",
        default="http://localhost:8045",
        action="store",
        help="website for tests",
    )


@pytest.fixture
def website(request):
    return request.config.getoption("--website")
