import pytest_bdd


# pytest_bdd.scenarios() is a helper method which:
# 1. finds all Feature files (*.feature) in the given path (features)
# 2. generates a pytest-bdd Scenario for each Scenario in the file

pytest_bdd.scenarios("features")
