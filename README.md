# Car Valuation Test Automation Framework

## Overview
This project is a test automation framework built using Python, Selenium, and BDD (Behavior-Driven Development) with `pytest-bdd`. It automates the process of verifying car valuation details from the [Motorway](https://motorway.co.uk/) website.

## Installation
### Prerequisites
- Python 3.8 or later
- Google Chrome browser
- ChromeDriver

### Setup Virtual Environment (Skip this if you have PyCharm setup and running)
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Running Tests
### Run BDD Tests
```sh
pytest --capture=no
Or
pytest --html=report.html  
```

### Run Standard Pytest Tests
```sh
pytest tests/
Or
pytest --html=report.html  
```

## Reports
Test reports are stored in `report.html`. Logging is managed via `utils/logger.py`.


## Logging
Test logs are stored in `test_log.log`. Logging is managed via `utils/logger.py`.

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

