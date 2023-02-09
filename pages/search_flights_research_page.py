import logging
import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils

class SearchFlightResults(BaseDriver):
    log= Utils.custom_logger(loglevel= logging.WARNING)
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    # Locators
    FILTER_BY_ONE_STOP_ICON= "//p[@class='font-lightgrey bold'][normalize-space()='1']"
    FILTER_BY_TWO_STOP_ICON= "//p[@class='font-lightgrey bold'][normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON= "//p[@class='font-lightgrey bold'][normalize-space()='0']"
    SEARCH_FLIHTS_RESULTS= "//spans[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]"
    def get_filter_by_one_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_ONE_STOP_ICON)

    def get_filter_by_two_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_TWO_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flights_results(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SEARCH_FLIHTS_RESULTS)

    def filter_flights_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_one_stop_icon().click()
            self.log.warning("Selected flights with one stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_two_stop_icon().click()
            self.log.warning("Selected flights with two stop")
            time.sleep(2)
        elif by_stop == "0 Stop":
            self.get_filter_by_non_stop_icon().click()
            self.log.warning("Selected non stop flights")
            time.sleep(2)
        else:
            self.log.warning("Please provide valid filter option")



