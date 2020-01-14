from pytest_bdd_splinter import *
import pytest
import pytest_bdd


@pytest.fixture(scope="session")
def browser_base_url():
    return "https://www.skyscanner.ca"
