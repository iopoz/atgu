from work_dir import driver
from selenium.common.exceptions import NoSuchElementException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page(object):
    def __init__(self):
        self.driver = driver.driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_element_by_path(self, path):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, path)))

    def wait_clickable_element_by_path(self, path):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, path)))
