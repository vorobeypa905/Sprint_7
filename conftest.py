import pytest
import help.new_courier as courier

@pytest.fixture
def create_new_courier():
    def _create_courier(create_fn):
        new_courier = create_fn()
        login = new_courier["login"]
        password = new_courier["password"]
        yield new_courier
        courier.delete_courier(login, password)
    return _create_courier


@pytest.fixture
def new_registered_courier(create_new_courier):
    generator = create_new_courier(courier.new_courier)
    return next(generator)


@pytest.fixture
def new_courier_not_registered(create_new_courier):
    generator = create_new_courier(courier.new_login_pass_fname)
    return next(generator)