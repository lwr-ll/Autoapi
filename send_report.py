import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://jenkisn5:123456@8.129.214.240:9000/job/wework/allure/widgets/suites.json"
        self.ding = 'https://oapi.dingtalk.com/robot/send?access_token=' \
                    'a5eb6e38be242dcf3a0ceaa1035a8c3093430de8da7384bf0b710711d4885c49'
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
                    "title": "猛犸象" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://jenkisn5:123456@8.129.214.240:9000/job/wework/allure/"
                }
            }
            response = requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
