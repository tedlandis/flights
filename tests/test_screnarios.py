import pytest_bdd

from pytest_bdd import given, when, then
from pytest_bdd.parsers import parse


# the following helper method performs two tasks:
# 1. finds all Feature (*.feature) files in the given folder (features)
# 2. generates a pytest-bdd Scenario for all Scenarios in each Feature file
pytest_bdd.scenarios('features')


@then(parse('I can see "{text}" on the page'))
def text_is_on_page(browser, text):
    assert browser.is_text_present(text)
    