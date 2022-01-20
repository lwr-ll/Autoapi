# 第二层的拆分 业务层
import jmespath
import pytest
from loguru import logger

from api.api_grouping import Grouping


class TestGrouping:
    def setup_class(self):
        self.group = Grouping()

    # 第四层拆分 剥离数据，进行参数化
    @pytest.mark.smoke
    @pytest.mark.parametrize("check",
                             [200],
                             ids=["ok"])
    def test_get_list(self, check):
        r = self.group.get_list(1)
        assert r.status_code == 200
        # assert jmespath.search("length[0]", r.json()) == 7
        # assert jmespath.search()

    @pytest.mark.parametrize("a,check",
                             [("#", 200), ("111", 200), ("qwe", 200)],
                             ids=["special", "int", "english"])
    def test_create_group(self, a, check):
        r = self.group.create_group(a)
        assert r.status_code == check


    # def test_add_company(self):
    #     r = self.group.get_list(1)
    #     id = self.group.jme_json("[?name=='wink'].id", r.json())
    #     res = self.group.add_company(id)
    #     assert res.status_code == 200
    #     assert jmespath.search("created_by", r.json()) == 181


    @pytest.mark.parametrize("a,check",
                             [("[?name=='#'].id", 200), ("[?name=='111'].id", 200), ("[?name=='qwe'].id", 200)],
                             ids=["special", "int", "english"])
    def test_delete_group(self, a, check):
        r = self.group.get_list(1)
        id = self.group.jme_json(a, r.json())
        res = self.group.delete_group(id)
        assert res.status_code == check
        assert res.status_code == 123


    @pytest.mark.smoke
    def test_all_group(self):
        self.group.create_group("小张")
        r = self.group.get_list(1)
        id = self.group.jme_json("[?name=='小张'].id", r.json())
        logger.info(id)
        self.group.add_company(id)
        r = self.group.delete_group(id)
        assert r.json() == 1