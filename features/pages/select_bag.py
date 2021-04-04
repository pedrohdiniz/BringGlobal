from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .base_page import BasePage

class SelectBag(BasePage):
    MESSAGE_FINISH_PLAN_CLASS = 'section-header__title section-header__title--desktop'

    def select_bag(self):
        self.driver.find_element(By.CSS_SELECTOR, ".card__item:nth-child(1) .ry-radio-circle-button__label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ry-button--gradient-yellow").click()
        self.driver.find_element(By.CSS_SELECTOR, ".enhanced-takeover__product-dismiss-cta").click()
        self.driver.find_element(By.CSS_SELECTOR, ".ry-button--full").click()
        element = self.driver.find_element(By.CSS_SELECTOR, ".action-badge--undefined > .action-badge__pillar-icon")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".action-badge__pillar-icon g > path")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, ".action-badge__pillar-icon > .icon-18 > svg")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()
        element = self.driver.find_element(By.CSS_SELECTOR,
                                           ".trip-planner__pillar-tab:nth-child(4) > .pillar-tab__button")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "body")
        actions = ActionChains(self.driver)
        actions.move_to_element(element, 0, 0).perform()


    def finish_plan(self):
        return self.wait_element_visibility(By.CLASS_NAME, self.MESSAGE_FINISH_PLAN_CLASS).text