class LoginCourierDataTest:

    required_fields = ["login","password"]

    success_login_status = 200

    bad_login_status = 400
    bad_login_message = "Недостаточно данных для входа"

    wrong_login_status = 404
    wrong_login_message = "Учетная запись не найдена"

