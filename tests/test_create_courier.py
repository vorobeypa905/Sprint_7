import allure
import pytest
import requests

from conftest import new_courier_not_registered
from data.url import Url
import help.new_courier as courier
from data.create_courier_test_data import CreateCourierDataTest as Dt


class TestCreateCourier:

    @allure.title("Проверка успешного создания курьера. Курьера можно создать.")
    def test_create_courier_success(self, new_courier_not_registered):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_courier_not_registered)
        assert response.status_code == Dt.success_status
        assert response.json()["ok"] == True

    @allure.title('Проверка создания одинаковых курьеров. Статус 409.')
    def test_create_courier_double_similar_couriers(self, new_registered_courier):
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=new_registered_courier)
        assert response.status_code == Dt.conflict_status
        assert response.json()["message"] == Dt.conflict_message

    @allure.title("Проверка создания курьера с отсутствующими обязательными полями.")
    @pytest.mark.parametrize('param', Dt.required_fields)
    def test_create_courier_required_fields_bad_request(self, param):
        payload = courier.new_login_pass_fname()
        del payload[param]
        url = Url.BASE_URL + Url.COURIER_URL
        response = requests.post(url=url, json=payload)
        assert response.json()["message"] == Dt.bad_message
        assert response.status_code == Dt.bad_status


