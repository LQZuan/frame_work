from page.add_member import AddMember
from page.base_page import BasePage


class AddManual(BasePage):
    def add_form(self, addMember):
        self._param["value"] = addMember
        self._param["phonenum"] = "138001380010"
        self.steps('../page/config/member_list.yaml')
        return AddMember(self._driver)