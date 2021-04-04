from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SelectFlight(BasePage):

    def select_price(self):
        self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c132-17 > .time:nth-child(3) > .h2").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".ry-button--outline-dark-blue:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c140-13 .item:nth-child(3) .price__decimals")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c140-13 .item:nth-child(3) .price__decimals").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ng-tns-c132-14 > .time:nth-child(3) > .time__city").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".ry-button--outline-dark-blue > .b3").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".login-touchpoint__login-later").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".ng-star-inserted:nth-child(1) > pax-passenger .dropdown__toggle").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown--opened > .dropdown__toggle svg").click()
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown__toggle--error svg").click()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".ng-star-inserted:nth-child(2) > .dropdown-item__link .dropdown-item__label").click()
        self.driver.find_element(By.ID, "formState.passengers.ADT-0.name").click()
        self.driver.find_element(By.ID, "formState.passengers.ADT-0.name").send_keys("Sonia ")
        self.driver.find_element(By.ID, "formState.passengers.ADT-0.surname").click()
        self.driver.find_element(By.ID, "formState.passengers.ADT-0.surname").send_keys("Pereira")
        self.driver.find_element(By.CSS_SELECTOR, "#title-0-error-message .dropdown__toggle").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "#title-0-error-message .dropdown__toggle")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".dropdown-item__link--highlighted .dropdown-item__label").click()
        self.driver.find_element(By.ID, "formState.passengers.ADT-1.name").click()
        self.driver.find_element(By.ID, "formState.passengers.ADT-1.name").send_keys("Diogo")
        self.driver.find_element(By.ID, "formState.passengers.ADT-1.surname").send_keys("Bettencourt")
        self.driver.find_element(By.ID, "formState.passengers.CHD-0.name").click()
        self.driver.find_element(By.ID, "formState.passengers.CHD-0.name").send_keys("Inês")
        self.driver.find_element(By.ID, "formState.passengers.CHD-0.surname").send_keys("Marçal")
        self.driver.find_element(By.CSS_SELECTOR, ".continue-flow__button").click()