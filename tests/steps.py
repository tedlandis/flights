from pytest_bdd import given, when, then
from pytest_bdd.parsers import parse as p


# Common Steps are defined in:
# https://github.com/labd/pytest-bdd-splinter/tree/master/src/pytest_bdd_splinter

@then(p('I can see "{text}" on the page'))
def text_is_on_page(browser, text):
    assert browser.is_text_present(text)
    