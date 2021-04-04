import time
import requests
import os
import random

dapr_port = os.getenv("DAPR_HTTP_PORT", 3500)
base_url = "http://localhost:{}/v1.0/invoke/{{}}/method/{{}}".format(dapr_port)


def post_neworder(app_id, num_of_start):
    n = num_of_start
    url = base_url.format(app_id, "neworder")

    def post_impl():
        nonlocal n
        try:
            message = {"data": {"orderId": n}}
            requests.post(url, json=message)
        except Exception as e:
            print(e)
        n += 1
    return post_impl


def get_order(app_id):
    url = base_url.format(app_id, "order")

    def get_impl():
        try:
            response = requests.get(url, json={})
            print(response)
        except Exception as e:
            print(e)
    return get_impl


nodeapp_neworder = post_neworder("nodeapp", random.randint(0, 1000))
nodeapp_order = get_order("nodeapp")
denoapp_neworder = post_neworder("denoapp", random.randint(0, 1000))
denoapp_order = get_order("denoapp")

print("start")


while True:
    nodeapp_neworder()
    time.sleep(0.5)

    denoapp_neworder()
    time.sleep(0.5)

    nodeapp_order()
    time.sleep(0.5)

    denoapp_order()
    time.sleep(0.5)

print("stop")
