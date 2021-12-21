import json
import requests

def storeConnectionSpeed():
    url = 'https://maker.ifttt.com/trigger/{event_name}/json/with/key/{key}'

    value1 = 1
    value2 = 2
    value3 = 3
    value4 = 4

    body = {}
    if value1 is not None:
        body['date'] = value1
    if value2 is not None:
        body['time'] = value2
    if value3 is not None:
        body['download'] = value3
    if value4 is not None:
        body['upload'] = value4

    response = requests.post(url, json=body)
    
    if response.status_code == 200:
        print("Connection speeds stored")
    else:
        print("something went wrong")
