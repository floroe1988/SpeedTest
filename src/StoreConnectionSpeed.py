import json
import requests

def storeConnectionSpeed():
    url = 'https://maker.ifttt.com/trigger/{event_name}/with/key/{key}'

    value1 = 1
    value2 = 2
    value3 = 3

    body = {}
        if value1 is not None:
            body['value1'] = value1
        if value2 is not None:
            body['value2'] = value2
        if value3 is not None:
            body['value3'] = value3

    response = requests.post(url, json=body)

    print("Connection speeds stored")
