import allure
import requests
import random
import string

from data.url import Url




@allure.step("Метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки")
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

@allure.step("Метод регистрации нового курьера возвращает список из логина и пароля")
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

@allure.step("Создание и регистрация курьера")
def new_courier():
    login_pass = register_new_courier_and_return_login_password()

    new_courier_data = {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }

    return new_courier_data
@allure.step("Метод создает случайного курьера")
def new_login_pass_fname():
    login_pass_fname = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

    return login_pass_fname

@allure.step("Получение id курьера, которого надо удалить")
def get_courier_id(login, password):
    payload = {
        "login": login,
        "password": password
    }
    response_login = requests.post(Url.BASE_URL + Url.COURIER_LOGIN_URL, json=payload)

    return response_login.json()["id"]

@allure.step("Удаление курьера")
def delete_courier(login, password):
    id = get_courier_id(login, password)
    url = f'{Url.BASE_URL}{Url.COURIER_URL}/{id}'
    response_delete = requests.delete(url=url)
