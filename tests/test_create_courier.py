import allure
import pytest
import requests

from conftest import new_courier_not_registered
from data.url import Url
import data.new_courier as courier
from data.create_courier_test_data import CreateCourierDataTest as Dt


class TestCreateCourier:

    @allure.title("Проверка успешного создания курьера. Курьера можно создать. Код 201")
    def test_create_courier_success_status(self, new_courier_not_registered):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_courier_not_registered)
        assert response.status_code == Dt.success_status

    @allure.title('Проверка создания одинаковых курьеров. Статус 409.')
    def test_create_courier_double_similar_couriers_status_code_409(self, new_registered_courier):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_registered_courier)
        assert response.status_code == Dt.conflict_status

    @allure.title("Проверка создания курьера с отсутствующими обязательными полями. Сообщение об ошибке. Отсутствует: {param}")
    @pytest.mark.parametrize('param', Dt.required_fields)
    def test_create_courier_required_fields_bad_request_message(self, param):
        payload = courier.new_login_pass_fname()
        del payload[param]

        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=payload)
        assert response.json()["message"] == Dt.bad_message

    @allure.title('Проверка успешного создания курьера. Успешный запрос возвращает {"ok":true};')
    def test_create_courier_success_response_ok_true(self, new_courier_not_registered):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_courier_not_registered)
        assert response.json()["ok"] == True

    @allure.title("Проверка создания курьера с отсутствующими обязательными полями. Код 400. Отсутствует: {param}")
    @pytest.mark.parametrize('param', Dt.required_fields)
    def test_create_courier_required_fields_bad_request_status_code(self, param):
        payload = courier.new_login_pass_fname()
        del payload[param]

        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=payload)
        assert response.status_code == Dt.bad_status

    @allure.title('Проверка создания пользователя с логином, который уже есть. Сообщение об ошибке.')
    def test_create_courier_double_similar_couriers_message(self, new_registered_courier):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_registered_courier)
        assert response.json()["message"] == Dt.conflict_message

