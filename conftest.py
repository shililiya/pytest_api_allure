import pytest
import requests
import json
from util.httpUtil import HttpUtil
from common.commonData import CommonDate

http = HttpUtil()

@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    data = {"userName":CommonDate.mobile,"password":CommonDate.password}
    resp_login = http.post('/sys/login',data)
    CommonDate.token = resp_login['object']['token']
    print("登录成功")
    # yield
    # resp_dict = json.loads(resp_login.text)
    # token = resp_dict['object']['token']  # 获取token
    # headers['token'] = token  # 将token加到headers的字典里
    #
    #  http = requests.session()
    # resp_logout = http.post(url="http://192.168.1.203:8083/sys/logout",
    #                      proxies=proxie,
    #                      data=None,
    #                      headers=headers)
    # assert resp_logout.status_code == 200

    # print("退出登录")
