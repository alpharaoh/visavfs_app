from typing import List
from visa_vfs_api.models import CountryCode, Option
from selenium.webdriver.support.select import Select

from visa_vfs_api.utils.driver import when_element_is_present


def get_appointment_login_link(apply_from: CountryCode, apply_to: CountryCode):
    return f"https://visa.vfsglobal.com/{apply_from.value}/en/{apply_to.value}/login"


def choose_selections(options: List[Option]):
    for o in options:
        Select(when_element_is_present(o.x_path, 1)).select_by_visible_text(o.option)
