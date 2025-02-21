from pytest_bdd import scenario, given, when, then, parsers
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from src.pages.car_valuation_page import CarValuationPage
from src.utils.data_reader import read_registration_numbers, read_expected_output
from src.utils.logger import setup_logger

logger = setup_logger()

@pytest.fixture(scope="module")
def setup():
    """Fixture to initialize and quit the browser."""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    car_page = CarValuationPage(driver)
    yield driver, car_page
    driver.quit()

@pytest.fixture(scope="module")
def test_data():
    """Fixture to store test data (populated by Given steps)."""
    return {"reg_numbers": [], "expected_results": {}, "actual_results": {}}

@scenario('../features/car_valuation.feature', 'Validate car details')
def test_validate_car_details():
    """BDD Scenario: Validate car details"""

@given(parsers.parse('a set of car reg numbers from input file "{input_file}"'))
def given_car_reg_numbers(input_file, test_data):
    """Given step to load registration numbers from the input file."""
    test_data["reg_numbers"] = read_registration_numbers(input_file)
    assert test_data["reg_numbers"], "No registration numbers found in input file!"
    logger.info(f"Loaded {len(test_data['reg_numbers'])} registration numbers from {input_file}")

@given(parsers.parse('the expected details for the car reg from output file "{output_file}"'))
def given_expected_details(output_file, test_data):
    """Given step to load expected car details from the output file."""
    test_data["expected_results"] = read_expected_output(output_file)
    assert test_data["expected_results"], "No expected results found in output file!"
    logger.info(f"Loaded expected results from {output_file}")

@when("performs check for each car on the motorway website")
def when_performs_car_check(setup, test_data):
    """When step: Searches car valuation for each reg number."""
    driver, car_page = setup

    for reg in test_data["reg_numbers"]:
        car_page.search_car(reg)
        make_model, year = car_page.get_car_details()
        test_data["actual_results"][reg] = {"make_model": make_model, "year": year}
        logger.info(f"Checked {reg}: Found {make_model}, {year}")

@then("verify car details from the website matches to output")
def then_verify_car_details(test_data):
    """Then step: Validate actual vs expected car details."""
    for reg, actual_data in test_data["actual_results"].items():
        expected_data = test_data["expected_results"].get(reg, {"make_model": "N/A", "year": "N/A"})

        assert actual_data["make_model"] == expected_data["make_model"], (
            f"Mismatch for {reg}: Expected {expected_data['make_model']}, Got {actual_data['make_model']}"
        )
        assert actual_data["year"] == expected_data["year"], (
            f"Mismatch for {reg}: Expected {expected_data['year']}, Got {actual_data['year']}"
        )

    logger.info("Car valuation test completed successfully!")
