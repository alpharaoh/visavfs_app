from visa_vfs_api.utils.driver import open_browser, when_element_is_present
from visa_vfs_api.utils.vfs import choose_selections, get_appointment_login_link
from visa_vfs_api.models import CountryCode, Option


X_PATH_EMAIL = '//*[@id="mat-input-0"]'
X_PATH_PASSWORD = '//*[@id="mat-input-1"]'
X_PATH_NEW_BOOKING_BUTTON = (
    "/html/body/app-root/div/app-dashboard/section[1]/div/div[2]/button"
)

EXAMPLE_EMAIL = "commitsnips@gmail.com"
EXAMPLE_PASSWORD = "Akaam2001@"

ENTER = "\n"


def login(email: str, password: str):
    when_element_is_present(X_PATH_EMAIL, 2).send_keys(email)
    when_element_is_present(X_PATH_PASSWORD).send_keys(password + ENTER)
    when_element_is_present(X_PATH_EMAIL).submit()


def start_new_booking():
    when_element_is_present(X_PATH_NEW_BOOKING_BUTTON, 2).click()


if __name__ == "__main__":
    url = get_appointment_login_link(CountryCode.Britain, CountryCode.Italy)
    open_browser(url)
    login(EXAMPLE_EMAIL, EXAMPLE_PASSWORD)
    start_new_booking()
    choose_selections(
        [
            Option(1, "Italy Visa Application Centre Edinburgh"),
            Option(3, "Italy UK VisaCategory"),
            Option(3, "Tourist"),
        ]
    )
