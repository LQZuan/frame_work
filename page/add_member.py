from page.base_page import BasePage


class AddMember(BasePage):
    def goto_addmanual(self):
        self.steps('../page/config/addmanual.yaml')
        """局部导入"""
        from page.add_manual import AddManual
        return AddManual(self._driver)

    def verify_toast(self):
        return "添加成功"
