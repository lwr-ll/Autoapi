import json

import jmespath
import requests


# 第三层 base 对api做基础支撑 发送请求 获取token
from faker import Faker


class BaseApi:
    def __init__(self):
        self.header = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": self.get_token()
        }

    def send(self, data):
        r = requests.request(**data)
        # print(1)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        # print(2)
        return r

    def get_token(self):
        data = {
            'url': "http://123.56.138.96:3012/api/ainews-user/user/login",
            'method': "post",
            'json': {'name': "lsj1",
                    'password': "123123"}
        }
        return self.send(data).json().get("access_token")
    # print(3)


    def get_groupid(self):
        fake = Faker(locale='zh-CN')
        data = {
            "method": "post",
            "url": "http://123.56.138.96:3012/api/ainews-user/company-group/create",
            "headers": self.header,
            "json": {
                "name": fake.name()
            }
        }
        return self.send(data).json().get("id")
    # print(4)

    @staticmethod
    def jme_json(sta: str, data: dict):
        return jmespath.search(sta, data)


if __name__ == '__main__':
    print(BaseApi().get_token())
    print(BaseApi().get_groupid())
