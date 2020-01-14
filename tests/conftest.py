from pytest import fixture


pytest_plugins = (
    "pytest_bdd_splinter", 
    "steps",
)

# fixtures

@fixture(scope="session")
def browser_base_url():
    return "https://www.skyscanner.ca"
