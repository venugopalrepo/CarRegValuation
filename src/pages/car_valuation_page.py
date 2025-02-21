import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.pages.base_page import BasePage
from src.utils.logger import setup_logger

logger = setup_logger()

class CarValuationPage(BasePage):
    SEARCH_BOX = (By.ID, "vrm-input")
    SUBMIT_BUTTON = (By.CLASS_NAME, "Value your car")
    RESULT_MAKE_MODEL = (By.XPATH, "//h1[@data-cy='vehicleMakeAndModel']")
    RESULT_YEAR = (By.XPATH, "//ul[@data-cy='vehicleSpecifics']/li[1]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'InfoBox-module__contentText-nlxc')]//div")
    BASE_URL = "https://motorway.co.uk/"

    def search_car(self, registration_number):
        self.open_url(self.BASE_URL)
        time.sleep(2)
        search_box = self.wait_for_element(self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(registration_number)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

    def get_car_details(self):
        try:
            error_element = self.driver.find_elements(*self.ERROR_MESSAGE)
            if error_element:
                return "ERROR", "ERROR"
            make_model = self.driver.find_element(*self.RESULT_MAKE_MODEL).text.strip()
            year = self.driver.find_element(*self.RESULT_YEAR).text.strip()
            return make_model, year
        except Exception:
            return "ERROR", "ERROR"
