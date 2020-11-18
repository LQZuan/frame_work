from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from page.base_page import BasePage


class Confirm(BasePage):
    def confirm(self, delMember):
        self.steps("../page/confirm.yaml")
        sleep(5)
        ele = self._driver.find_elements(MobileBy.XPATH, f'//*[@text="Abc"]/..//*[@text="{delMember}"]')
        print(ele)
        print(len(ele))
        if len(ele) > 0:
            return False
        else:
            return True
