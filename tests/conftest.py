import pytest

import niobium  # noqa: F401


def pytest_addoption(parser):
    parser.addoption(
        "--website",
        default="http://localhost:8878",
        action="store",
        help="website for tests",
    )


@pytest.fixture
def website(request):
    return request.config.getoption("--website")
