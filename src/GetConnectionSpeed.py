from datetime import datetime
import speedtest

def getConnectionSpeed():
    '''
    Performes speedtest for down- and upload speed. Result is stored together with 
    the current date and time into a dictionary
    
    Return
    ---------
    result: dict
        Dictionary conatianing the entries {date (str: dd/mm/YY)}, {time (str: H:M:S)},
	{download (int: Mbit/s)} and {upload (int: Mbit/s)}
    '''
	
    # datetime object containing current date and time
    now = datetime.now()
	
    # dd/mm/YY
    date = now.strftime("%d/%m/%Y")
	
    # H:M:S
    time = now.strftime("%H:%M:%S")

    # performing speedtest
    s = speedtest.Speedtest()
    download = int((s.download()/1048576))	# convert bit/s to Mbit/s
    upload = int((s.upload()/1048576))		# convert bit/s to Mbit/s

    # write speedtest result to output data
    result = {}
    result['date'] = date
    result['time'] = time
    result['download'] = download
    result['upload'] = upload

    return(result)
