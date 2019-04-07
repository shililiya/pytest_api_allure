import requests
import json
from common.commonData import CommonDate
class HttpUtil:
    def __init__(self):
        self.http = requests.session()
        self.headers = {'Content-Type': 'application/json;charset=utf-8'}
    def post(self,path,data):
        host = CommonDate.host
        proxies = CommonDate.proxies
        data_json =json.dumps(data)
        if CommonDate.token is not None:
            self.headers['token'] = CommonDate.token
        resp_login = self.http.post(url=host+path,
                               proxies=proxies,
                               data=data_json,
                               headers=self.headers)
        assert resp_login.status_code == 200
        resp_json = resp_login.text
        resp_dict = json.loads(resp_json)
        return resp_dict