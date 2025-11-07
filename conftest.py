import pytest
import data.new_courier as courier

@pytest.fixture
def new_registered_courier():
    new_courier = courier.new_courier()
    login = new_courier["login"]
    password = new_courier["password"]
    yield new_courier
    courier.delete_courier(login, password)


@pytest.fixture
def new_courier_not_registered():
    new_courier = courier.new_login_pass_fname()
    login = new_courier["login"]
    password = new_courier["password"]
    yield new_courier
    courier.delete_courier(login, password)
