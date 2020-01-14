import pytest_bdd


# the following helper method performs two tasks:
# 1. finds all Feature (*.feature) files in the given folder (features)
# 2. generates a pytest-bdd Scenario for all Scenarios in each Feature file

pytest_bdd.scenarios('features')
