from time import sleep
from typing import List
from visa_vfs_api.models import CountryCode, Option

from visa_vfs_api.utils.driver import when_element_is_present


def get_appointment_login_link(apply_from: CountryCode, apply_to: CountryCode):
    return f"https://visa.vfsglobal.com/{apply_from.value}/en/{apply_to.value}/login"


def choose_selections(options: List[Option]):
    print(options)
    for o in options:
        print(o.x_path)
        when_element_is_present(o.x_path, 1).click()
        sleep(1)
