from time import sleep

from selenium.common.exceptions import (
    ElementClickInterceptedException,
    ElementNotInteractableException,
    ElementNotSelectableException,
    ElementNotVisibleException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from visa_vfs_api import driver

MAX_INTERCEPTION_ATTEMPTS = 5


def when_element_is_present(xpath: str, initial_wait: int = 0):
    sleep(initial_wait)
    return WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )


def attempt_click(x_path: str):
    error = False
    for attempt in range(MAX_INTERCEPTION_ATTEMPTS):
        try:
            when_element_is_present(x_path, 1).click()
            if error:
                print(f"Succeeded after {attempt+1} attempts")
                break
        except (
            ElementClickInterceptedException,
            ElementNotVisibleException,
            ElementNotInteractableException,
            ElementNotSelectableException,
            NoSuchElementException,
        ):
            error = True
            print(
                f"Failed to click {x_path}, trying again in 1s (attempt {attempt+1}/{MAX_INTERCEPTION_ATTEMPTS})"
            )
            sleep(1)


def open_browser(url: str):
    driver.get(url)
