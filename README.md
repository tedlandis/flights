# Flight Schedule Testing

This project demonstrates *pytest-bdd* based gherkin functional testing from a python virtual environment.

It tests website functionality using a selenium browser interface to interact with a flight scheduling website.

In order to keep the Step Definition python code accessible to the largest audience, two layers of abstraction are used.

The standard python *selenium* module is wrapped by *splinter*, an abstraction layer which provides a more pythonic access to the Selenium WebDriver.

Splinter itself is partially wrapped by *pytest-bdd-splinter*, via a set of common Step definitions which can be used in *pytest-bdd* Scenarios.

The common Steps defined in *pytest-bdd-splinter* are then seamlessly extended with custom Step definitions by either making calls to Splinter methods or directly to the Selenium Webdriver if required.

### To Do:

- migrate the tests from the virtual environment to a docker container
- run tests against standard selenium grid docker containers
- add support for Page Objects

## MacOS Setup

1. Install brew

    `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

2. Install Python 3.7

    `brew install python3.7`

3. Install pipenv

    `brew install pipenv`

4. Install geckodriver for Firefox

    `brew install geckodriver`

5. Install Firefox from `getfirefox.com`

## Python Virtual Environment Setup

    cd flights
    pipenv install

## Run Tests

    pipenv shell
    pytest
