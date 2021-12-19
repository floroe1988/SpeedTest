import speedtest

def getConnectionSpeed():
	s = speedtest.Speedtest()
	print("My download speed is:", s.download())
	print("My upload speed is:", s.upload())
	print("Connection speeds tested")