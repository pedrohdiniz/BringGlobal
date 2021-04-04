from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SelectSeat(BasePage):

    def select_seat(self):
        elf.driver.find_element(By.CSS_SELECTOR, ".seats-modal__cta").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--19 .ng-star-inserted:nth-child(7)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--18 .ng-star-inserted:nth-child(3)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".seatmap__seatrow--18 > .seatmap__seats > .ng-star-inserted:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".seatmap__seatrow--18 > .seatmap__seats > .ng-star-inserted:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--18 .ng-star-inserted:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".seatmap__seatrow--18 > .seatmap__seats > .ng-star-inserted:nth-child(2)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seat-text:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--18 .ng-star-inserted:nth-child(3)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".seatmap__seatrow--18 > .seatmap__seats > .ng-star-inserted:nth-child(3)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".ry-button").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--24 .seatmap__seat:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".seatmap__seatrow--with-band:nth-child(17) > .seatmap__seats > .ng-star-inserted:nth-child(1) svg")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".seatmap__seats:nth-child(3) > .ng-star-inserted:nth-child(1) svg")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".seatmap__seatrow--18 > .seatmap__seats > .ng-star-inserted:nth-child(1)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".seatmap__seatrow--18 > .seatmap__seats > .ng-star-inserted:nth-child(1)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--18 .ng-star-inserted:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".seatmap__seatrow--18 > .seatmap__seats > .ng-star-inserted:nth-child(2)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seat-text:nth-child(2)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--18 .ng-star-inserted:nth-child(3)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".seatmap__seatrow--18 > .seatmap__seats > .ng-star-inserted:nth-child(3)").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--18 .ng-star-inserted:nth-child(5)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--18 .ng-star-inserted:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--19 .ng-star-inserted:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--18 .ng-star-inserted:nth-child(5)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".seatmap__seatrow--24 .ng-star-inserted:nth-child(7)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".ry-button").click()
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(By.CSS_SELECTOR, ".enhanced-takeover-beta__product-dismiss-cta").click()