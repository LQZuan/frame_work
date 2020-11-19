from page.Search import Search
from page.add_member import AddMember
from page.base_page import BasePage


class Contact(BasePage):
    def goto_search(self):
        self.steps("../page/config/contact.yaml")
        return Search(self._driver)

    def goto_addmember(self):
        self.steps("../page/config/addmember.yaml")
        return AddMember(self._driver)
