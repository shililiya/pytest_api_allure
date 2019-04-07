from common.commonData import CommonDate
import pytest
from  conftest import http
import allure

@pytest.mark.info
@allure.feature('展示用户信息模块')
class Test_loadUserList(object):
    @allure.story('注册成功')
    def test_register(self):
        data = {"nickName":"啦啦ya",
                "userName":"15969854723",
                "telNo":"",
                "email":"",
                "address":"",
                "roleIds":"1",
                "regionId":1,
                "regionLevel":1}
        resp = http.post('/user/saveOrUpdateUser',data)
        print("注册成功")
        nickName = data["nickName"]
        userName = data["userName"]
        userId = self.login(userName)
        self.get(userId,nickName)

    @allure.story('登录成功')
    def login(self,userName):
        data = {"userName": userName,
                "password": CommonDate.password}
        resp = http.post('/sys/login',data)
        print("登录成功")
        assert resp['code'] == 200
        return resp['object']['userId']

    @allure.story('获取成功')
    def get(self,userId,nickName):
        data = {'pageSize':30,
                'pageCurrent':1}
        resp = http.post('/user/loadUserList',data)
        print("获取成功")
        assert resp['object']['list'][0]['id'] == userId
        assert resp['object']['list'][0]['nickName'] == nickName