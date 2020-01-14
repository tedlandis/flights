# Flight Schedule Testing

### MacOS Setup

1. Install brew

    `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

2. Install Python 3.7

    `brew install python3.7`

2. Install pipenv

    `brew install pipenv`

## Installation

Unzip into a workspace directory and set up the python virtual environment:

    cd flights
    pipenv install
    pipenv shell

## Run Tests

    pytest
