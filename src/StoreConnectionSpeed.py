import requests

def storeConnectionSpeed():
    url = 'https://maker.ifttt.com/trigger/{event_name}/json/with/key/{key}'

    value1 = 1
    value2 = 2
    value3 = 3
    value4 = 4

    body = {}
    body['date'] = value1
    body['time'] = value2
    body['download'] = value3
    body['upload'] = value4

    response = requests.post(url, json=body)
    
    if response.status_code == 200:
        print("Connection speeds stored")
    else:
        print("something went wrong")
