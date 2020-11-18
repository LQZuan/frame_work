from page.add_member import AddMember
from page.base_page import BasePage


class AddManual(BasePage):
    def add_form(self, addMember):
        self._param["value"] = addMember
        self._param["phonenum"] = "13800138000"
        self.steps('../page/member_list.yaml')
        return AddMember(self._driver)