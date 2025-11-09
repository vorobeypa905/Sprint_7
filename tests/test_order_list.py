import requests
import allure
from data.url import Url


class TestOrderList:

    @allure.title("Проверка успешного получения списка заказов. Код 200")
    def test_order_list_status_success(self):
        url = Url.BASE_URL + Url.ORDER_URL
        response = requests.get(url=url)
        assert response.status_code == 200

    @allure.title("Проверка успешного получения списка заказов. Список не пустой")
    def test_order_list_order_list_is_not_empty(self):
        url = Url.BASE_URL + Url.ORDER_URL
        response = requests.get(url=url)
        assert len(response.json()["orders"]) > 0