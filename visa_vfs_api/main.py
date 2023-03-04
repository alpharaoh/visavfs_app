from visa_vfs_api.models import CountryCode, Option
from visa_vfs_api.utils.driver import open_browser, when_element_is_present
from visa_vfs_api.utils.vfs import (
    attempt_click,
    get_appointment_login_link,
    select_dropdown_options,
)

EXAMPLE_EMAIL = "commitsnips@gmail.com"
EXAMPLE_PASSWORD = "Akaam2001@"
X_PATH_EMAIL = '//*[@id="mat-input-0"]'
X_PATH_PASSWORD = '//*[@id="mat-input-1"]'
X_PATH_NEW_BOOKING_BUTTON = (
    "/html/body/app-root/div/app-dashboard/section[1]/div/div[2]/button"
)
ENTER_KEY = "\n"


def login(email: str, password: str):
    when_element_is_present(X_PATH_EMAIL, 2).send_keys(email)
    when_element_is_present(X_PATH_PASSWORD).send_keys(password + ENTER_KEY)
    when_element_is_present(X_PATH_EMAIL).submit()


if __name__ == "__main__":
    url = get_appointment_login_link(CountryCode.Britain, CountryCode.Italy)
    open_browser(url)
    login(EXAMPLE_EMAIL, EXAMPLE_PASSWORD)
    attempt_click(X_PATH_NEW_BOOKING_BUTTON)
    select_dropdown_options(
        [
            Option(1, "Italy Visa Application Centre Edinburgh"),
            Option(3, "Italy UK VisaCategory"),
            Option(3, "Tourist"),
        ]
    )
