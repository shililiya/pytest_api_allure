from common.commonData import CommonDate
from  conftest import http
import allure

@allure.feature('登录模块')
class Test_login():

    @allure.story('登录成功')
    def test_login_success(self):
        data = {"userName": CommonDate.mobile,
                "password": CommonDate.password}
        resp = http.post('/sys/login',data)
        assert resp['code'] == 200
        assert  resp['msg']  == '操作成功'
        assert resp['object']['userId'] == 153

    @allure.story('密码错误时登录')
    def test_login_passwordError(self):
        data = {"userName": "15935156290",
                "password": "12389797"}
        resp = http.post('/sys/login', data)
        assert resp['code'] == 410
        assert resp['msg'] == '用户名或密码错误'

    @allure.story('用户名不存在时登录')
    def test_login_username_not_exists(self):
        data = {"userName":"18210034706hjghjghjgjh",
                "password":"123456"}
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'

    @allure.story('用户名为空时登录')
    def test_login_username_null(self):
        data = {"userName":"",
                "password":"123456"}
        resp = http.post('/sys/login', data)
        assert resp['code'] == 3010
        assert resp['msg'] == '此账户禁止登录'

    @allure.story('用户名参数不存在时登录')
    def test_login_usernameParm_not_exist(self):
        data = {
                "password":"123456"}
        resp = http.post('/sys/login', data)
        assert resp['code'] == 301
        assert resp['msg'] == '用户不存在'

