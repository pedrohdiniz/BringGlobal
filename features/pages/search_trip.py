from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .base_page import BasePage


class SearchTrip(BasePage):
    BUTTON_PRIVACY_CLASS = 'cookie-popup-with-overlay__button'
    FROM_ID = 'input-button__departure'
    TO_ID = 'input-button__destination'

    def search_flights(self):
        self.click_element(By.CLASS_NAME, self.BUTTON_PRIVACY_CLASS)
        self.driver.find_element(By.ID, self.FROM_ID).click()
        self.driver.find_element(By.ID, self.FROM_ID).clear()
        self.write_in_element(By.ID, self.FROM_ID, 'Lisbon')
        self.driver.find_element(By.ID, self.TO_ID).click()
        self.driver.find_element(By.ID, self.TO_ID).clear()
        self.write_in_element(By.ID, self.TO_ID, 'Paris Beauvais')
        self.driver.find_element(By.CSS_SELECTOR, ".flight-search-widget__start-search").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ng-trigger-datesFromTripTypeChange .input-button__input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".m-toggle__button:nth-child(3) path").click()
        self.driver.find_element(By.CSS_SELECTOR, ".m-toggle__scrollable-item:nth-child(9) > .m-toggle__month").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".datepicker__calendar--left .calendar-body__row:nth-child(3) > .calendar-body__cell-wrap:nth-child(1) > .calendar-body__cell").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".datepicker__calendar--left .calendar-body__row:nth-child(3) > .calendar-body__cell-wrap:nth-child(19) > .calendar-body__cell").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c194-9 .image-wrapper__image")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".passengers-picker__passenger-type:nth-child(3) .counter__button-wrapper--enabled").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".passengers-picker__passenger-type:nth-child(5) .counter__button-wrapper--enabled").click()
        self.driver.find_element(By.CSS_SELECTOR, ".flight-search-widget__start-search").click()



