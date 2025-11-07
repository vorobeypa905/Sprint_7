import allure
import pytest
import requests

from data.login_courier_test_data import LoginCourierDataTest as Dt
from data.url import Url


class TestLoginCourier:
    @allure.title("Проверка успешной авторизации. Курьер авторизуется")
    def test_courier_authorization_success(self, new_registered_courier):
        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=new_registered_courier)
        assert response.status_code == Dt.success_login_status

    @allure.title("Проверка успешной авторизации. Запрос возвращает id")
    def test_courier_authorization_success_id(self, new_registered_courier):
        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=new_registered_courier)
        assert response.json()["id"]

    @allure.title("Проверка входа с неправильными данными. Код 404.")
    @pytest.mark.parametrize('param', Dt.required_fields)
    def test_courier_error_login_status(self, param, new_registered_courier):
        new_registered_courier[param] += "error"
        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=new_registered_courier)
        assert response.status_code == Dt.wrong_login_status

    @allure.title("Проверка входа с неправильными данными.  Сообщение об ошибке.")
    @pytest.mark.parametrize('param', Dt.required_fields)
    def test_courier_error_login_message(self, param, new_registered_courier):
        new_registered_courier[param] += "error"
        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=new_registered_courier)
        assert response.json()["message"] == Dt.wrong_login_message


    @allure.title("Проверка входа с неполными данными.Код 400.")
    @pytest.mark.parametrize('param', Dt.required_fields)
    def test_courier_login_required_fields_bad_login_status_code(self, param, new_registered_courier):
        payload = {param: new_registered_courier[param]}
        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=payload)
        if response.status_code == 504:
            pytest.skip("Server timeout (504)")
        assert response.status_code == Dt.bad_login_status

    @allure.title("Проверка входа с неполными данными. Сообщение об ошибке.")
    @pytest.mark.parametrize('param', Dt.required_fields)
    def test_courier_login_required_fields_bad_login_message(self, param, new_registered_courier):
        payload = {param: new_registered_courier[param]}
        url = Url.BASE_URL + Url.COURIER_LOGIN_URL
        response = requests.post(url=url, json=payload)
        if response.status_code == 504:
            pytest.skip("Server timeout (504)")
        assert response.json()["message"] == Dt.bad_login_message




