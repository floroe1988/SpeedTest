import requests

def storeConnectionSpeed(payload):
    '''
    Funtcion triggers the ifttt event specified in the tag {event_name}. This event
    has to be specified in the url variable together with the {key} provided by ifttt
    for the respective account.
    
    For this function to work, the event must be created in the user's ifttt account.
    
    Parameters
    ----------
        payload: dict
            The payload has to contain the following entrie {date (str)}, {time (str)},
            {download (int)} and {upload (int)}
    '''
    
    # define ifttt webhook url
    url = 'https://maker.ifttt.com/trigger/{event_name}/json/with/key/{key}'

    # api call to ifttt webhook
    response = requests.post(url, json=payload)
    
    # print out result of url request
    if response.status_code == 200:
        print("Connection speeds stored")
    else:
        print("something went wrong")
