from time import sleep

from page.base_page import BasePage
from page.contact import Contact


class Main(BasePage):
    def goto_contact(self):
        sleep(5)
        self.steps("../page/config/main.yaml")
        return Contact(self._driver)