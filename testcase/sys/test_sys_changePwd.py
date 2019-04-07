import pytest
from common.commonData import CommonDate
from  conftest import http
import allure

@allure.feature('修改密码模块')
class Test_changePwd(object):
    @allure.story('修改密码成功')
    @pytest.mark.usefixtures("recoveryPwd")
    def test_changePwd(self):
        newPwd = '111111'
        data = {"userId":153,
                "userName":"15935156290",
                "oldPwd":CommonDate.password,
                "password":newPwd}
        resp = http.post('/sys/changePwd', data)
        assert resp['code'] == 200
        assert resp['msg'] == "操作成功"
@pytest.fixture()
def recoveryPwd():
    newPwd = '111111'
    yield
    data = {"userId":153,
            "userName":"15935156290",
            "oldPwd":newPwd,
            "password":CommonDate.password}
    resp = http.post('/sys/changePwd', data)
    assert resp['code'] == 200
    assert resp['msg'] == "操作成功"
