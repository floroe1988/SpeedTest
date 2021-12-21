import requests

def storeConnectionSpeed(payload):
    # define ifttt webhock url
    url = 'https://maker.ifttt.com/trigger/{event_name}/json/with/key/{key}'

    # api call to ifttt webhook
    response = requests.post(url, json=payload)
    
    # print out result of url request
    if response.status_code == 200:
        print("Connection speeds stored")
    else:
        print("something went wrong")
