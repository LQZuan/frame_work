import pytest
import yaml

from page.app import App


class TestAddContact:
    @pytest.mark.parametrize("addMember", yaml.safe_load(open("./addmember.yaml")))
    def test_addcontact(self, addMember):
        """
        测试逻辑：
        :param delMember:
        :return:
        """
        assert App().start().main().goto_contact().goto_addmember().goto_addmanual().add_form(addMember).goto_addmanual() == "保存成功"
