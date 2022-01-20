import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://admin:Aa123456!@123.57.2.141:9000/job/Autoapi/allure/widgets/suites.json"
        self.ding = 'https://oapi.dingtalk.com/robot/send?access_token=42ca91c90da3f450aa09488b7676365b76e0b404f0968c03be039f7d19a40196'
        self.error = self.get_allure_error()

    def get_allure_error(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "账号jenkisn5,密码123456",
                    "title": "," + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://admin:Aa123456!@123.57.2.141:9000/job/Autoapi/allure/"
                }
            }
            response = requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
