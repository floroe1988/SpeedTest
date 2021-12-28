[![CI](https://github.com/floroe1988/SpeedTest/actions/workflows/main.yml/badge.svg)](https://github.com/floroe1988/SpeedTest/actions/workflows/main.yml)

# SpeedTest
Python functionality to automate cyclical network speedtests and sync result to google
spread sheet

## Setup IFTTT
To store the results of the speedtest a corresponding webhook template has to be created 
inside IFTTT.  
To do so, first create a new template with a "webhook" containing a json payload as trigger
![IFTTT Trigger](docs/Trigger.png)

As resulting action configure a "add row to spreadsheet" action (the entries for the
formatting do not matter, as these will be overwritten by the filter code which will
be applied later)
![IFTTT Action](docs/Action.png)

Apply the following filter code to the IFTTT template. This filter code is required to 
have the json payload written into the spreadsheet in a structured manner.
![IFTTT FilterCoce](docs/FilterCode.png)
```
let payload = JSON.parse(MakerWebhooks.jsonEvent.JsonPayload)
let formattedRow = `${payload.date}|||${payload.time}|||${payload.download}|||${payload.upload}`
GoogleSheets.appendToGoogleSpreadsheet.setFormattedRow(formattedRow)
```

## Setup Edge Device
Clone repository to your local device
```
git clone https://github.com/floroe1988/SpeedTest.git
```

To make the application work with the IFTTT webhook some changes are required
inside the file [`storeConnectionSpeed`](https://github.com/floroe1988/SpeedTest/blob/main/src/StoreConnectionSpeed.py)  
Inside the file the element {event_name} inside the url has to be changed to the event name
specified inside the IFTTT remplate. Additionally the element {key} has to be replaced with 
the presonal access key provided for the respective IFTTT account.
![Python FileConfig](docs/FileConfig.png)

Setup a virtual environment where the applcation can live in and source it
```
python3 -m venv ~/.SpeedTest
source ~/.SpeedTest/bin/activate
```

cd into the cloned directory and run the following commant
```
make install
```

## Running the application
To start the applikation on the edge device, run the following command
```
python3 main.py
```

Once the application is running it will perform a speedtest every 10 minutes and store the result
inside the google spreadsheet which is defined in the IFTTT template. The result contains the 
current date and time as well as the download and upload speed.
