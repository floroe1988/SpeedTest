from datetime import datetime
import speedtest

def getConnectionSpeed():
    # datetime object containing current date and time
    now = datetime.now()
	
	# dd/mm/YY
    date = now.strftime("%d/%m/%Y")
	
	# H:M:S
    time = now.strftime("%H:%M:%S")

    # performing speedtest
    s = speedtest.Speedtest()
    download = (s.download()/1048576)
    upload = (s.upload()/1048576)

    # write speedtest result to output data
    result = {}
    result['date'] = date
    result['time'] = time
    result['download'] = download
    result['upload'] = upload
    print("Connection speeds tested")

    return(result)