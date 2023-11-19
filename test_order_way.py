#Попова Елена, 10 когорта, Финальный проект, Инженер по тестированию плюс
import config
import requests
import data

# Функция создания нового заказа
def post_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH,
                         json=body)

responce = post_new_order(data.body_order)

#Сохранили номер заказа

my_order_number = responce.json()["track"]


def get_status_order():
    return requests.get(config.URL_SERVICE + config.TRACK_ORDER_PATH + "?t=" + str(my_order_number))

responce = get_status_order()

def test_get_status_order():
    responce = get_status_order()
# Проверяется, что код ответа равен 200
    assert responce.status_code == 200
