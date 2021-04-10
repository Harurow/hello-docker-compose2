import time
import requests
import os
import sys
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
            print("ok: POST {0} / neworder".format(app_id))
        except Exception as e:
            print(e)
        n += 1
    return post_impl


def get_order(app_id):
    url = base_url.format(app_id, "order")

    def get_impl():
        try:
            response = requests.get(url, json={})
            print("ok: GET {0} / order > {1}".format(app_id, response.text))
        except Exception as e:
            print(e)
    return get_impl


nodeapp_neworder = post_neworder("nodeapp", random.randint(0, 1000))
nodeapp_order = get_order("nodeapp")

denoapp_neworder = post_neworder("denoapp", random.randint(0, 1000))
denoapp_order = get_order("denoapp")

goapp_neworder = post_neworder("goapp", random.randint(0, 1000))
goapp_order = get_order("goapp")


def main():
    print("start")

    while True:
        nodeapp_neworder()
        time.sleep(0.2)

        denoapp_neworder()
        time.sleep(0.2)

        goapp_neworder()
        time.sleep(0.2)

        nodeapp_order()
        time.sleep(0.2)

        denoapp_order()
        time.sleep(0.2)

        goapp_order()
        time.sleep(0.2)

    print("stop")


if __name__ == '__main__':
    if (len(sys.argv) > 1) and (sys.argv[1] == "debug"):
        import ptvsd
        print("waiting...")
        ptvsd.enable_attach(address=('0.0.0.0', 9229))
    main()
