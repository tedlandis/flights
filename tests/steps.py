from pytest_bdd import given, when, then
from pytest_bdd.parsers import parse as p


@then(p('I can see "{text}" on the page'))
def text_is_on_page(browser, text):
    assert browser.is_text_present(text)
    