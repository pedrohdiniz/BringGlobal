from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    TIMEOUT = 60
    POLLING = 100
    URL = None
    context = None

    def __init__(self, driver):
        self.driver = driver

    def wait_element_by_locator(self, locator, element):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located((locator, element)))

    def wait_element_visibility(self, locator, element):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located((locator, element)))

    def wait_element_clickable(self, locator, element):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable((locator, element)))

    def wait_element_invisibility(self, locator, element):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.invisibility_of_element_located((locator, element)))

    def find_elements(self, locator, element):
        return self.driver.find_elements(locator, element)

    def click_element(self, locator, element):
        button = self.wait_element_clickable(locator, element)
        button.click()

    def write_in_element(self, locator, element, text):
        element = self.wait_element_clickable(locator, element)
        element.send_keys(text)

    def clear_text_in_element(self, locator, element):
        element = self.wait_element_clickable(locator, element)
        element.clear()
