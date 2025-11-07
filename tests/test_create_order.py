import requests
import allure
import pytest
import json

from data.url import Url
from data.create_order_test_data import CreateOrderTestData as Dt


class TestCreateOrder:

    @allure.title("Проверка успешного создания заказа. Заказ с одним цветом: {color}")
    @pytest.mark.parametrize('color', Dt.available_color)
    def test_create_order_one_color(self, color):
        order_data = Dt.order_data(color)
        url = Url.BASE_URL + Url.ORDER_URL
        response = requests.post(url=url, json=order_data)
        assert response.status_code == Dt.success_status

    @allure.title("Проверка успешного создания заказа. Заказ с двумя цветами")
    def test_create_order_two_colors(self):
        order_data = Dt.order_data(Dt.available_color)
        url = Url.BASE_URL + Url.ORDER_URL
        response = requests.post(url=url, json=order_data)
        assert response.status_code == Dt.success_status

    @allure.title("Проверка успешного создания заказа. Цвет не передается")
    def test_create_order_not_color(self):
        order_data = Dt.order_data()

        url = Url.BASE_URL + Url.ORDER_URL
        payload = json.dumps(order_data)
        response = requests.post(url=url, data=payload)
        assert response.status_code == Dt.success_status

    @allure.title("Проверка успешного создания заказа. В ответе присутствует track")
    def test_create_order_track_in_response(self):
        order_data = Dt.order_data()
        url = Url.BASE_URL + Url.ORDER_URL
        response = requests.post(url=url, json=order_data)
        assert response.json()["track"]