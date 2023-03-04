from time import sleep
from typing import List

from visa_vfs_api.models import CountryCode, Option
from visa_vfs_api.utils.driver import attempt_click


def get_appointment_login_link(apply_from: CountryCode, apply_to: CountryCode):
    return f"https://visa.vfsglobal.com/{apply_from.value}/en/{apply_to.value}/login"


def select_dropdown_options(options: List[Option]):
    for o in options:
        print(o.x_path)
        attempt_click(o.x_path)
        sleep(1)
