from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from visa_vfs_api import driver


def when_element_is_present(xpath: str, initial_wait: int = 0):
    sleep(initial_wait)
    return WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def open_browser(url: str):
    driver.get(url)
