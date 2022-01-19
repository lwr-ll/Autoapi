# 第一层 api层 封装我们接口 为了我们后期的业务调用
from faker import Faker

from api.base_api import BaseApi


class Grouping(BaseApi):
    def get_list(self, num):
        """
        获取分组信息
        :param num:
        :return:
        """
        data = {
            "method": "get",
            "url": "http://123.56.138.96:3012/api/ainews-user/company-group/user-custom-group",
            "headers": self.header,
            "params": {
                "page": num,
                "per_page": 10,
                "start_time": "2021-12-30",
                "end_time": "2022-01-13"
            }
        }
        print(1)
        return self.send(data)

    def create_group(self, a):
        """
        添加分组
        :return:
        """
        # fake = Faker(locale='zh-CN')
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-user/company-group/create",
            "headers": self.header,
            "json": {
                # "name": fake.name()
                "name": a
            }
        }
        print(2)
        return self.send(data)

    def add_company(self, id):
        # self.create_group()
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-user/company-group/company-create",
            "headers": self.header,
            "json": {
                # "group_id": self.get_groupid(),
                "group_id": id,
                "company_code": "000001"
            }
        }
        print(3)
        return self.send(data)

    def delete_group(self, id):
        data = {
            "params": {
                # "id": self.get_groupid()
                "id": id
            },

            "method": "get",
            "url": "http://123.56.138.96:3012/api/ainews-user/company-group/delete",
            "headers": self.header
        }
        return self.send(data)




if __name__ == '__main__':
    case = Grouping()
    # case.get_list(num=1)
    case.create_group()
    case.add_company()
    # case.delete_group()
