import pytest
import yaml

from page.app import App


class TestDelContact:
    @pytest.mark.parametrize("delMember", yaml.safe_load(open("test_data/test.yaml")))
    def test_delcontact(self, delMember):
        """
        测试逻辑：
        :param delMember:
        :return:
        """
        assert App().start().main().goto_contact().goto_search().search(
            delMember).goto_edit().edit_member().del_member().confirm(delMember)
