class CreateOrderTestData:

    success_status = 201
    available_color = ["BLACK", "GREY"]

    @staticmethod
    def order_data(color=None):
        data = {
            "firstName": "Samokat",
            "lastName": "Petrovich",
            "address": "Moscow, Red platz",
            "metroStation": 5,
            "phone": "+7 965 777 88 99",
            "rentTime": 3,
            "deliveryDate": "2025-11-11",
            "comment": "Go"
        }

        if color is not None:
            if isinstance(color, list):
                data["color"] = color
            else:
                data["color"] = [color]
        else:
            pass

        return data
