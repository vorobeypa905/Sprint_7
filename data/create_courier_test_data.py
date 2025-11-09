class CreateCourierDataTest:
    required_fields = ["login", "password"]

    success_status = 201
    success_response = {'ok': True}

    bad_status = 400
    bad_message = "Недостаточно данных для создания учетной записи"

    conflict_status = 409
    conflict_message = "Этот логин уже используется. Попробуйте другой."