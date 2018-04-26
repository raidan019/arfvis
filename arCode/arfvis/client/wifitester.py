import socket
import sys
from subprocess import call
from wifi import Cell
from pynmea import nmea
import urllib.request
import time
import json

#Client to report wifi data to a Django server using HTTP PUT
def sendSignals(server):

    enctype = 5
    signal = {
        "sensor": 1,
        "device" : "linksys",
        "azimuth": 20,
        "signal_strength": 64,
        "sensor_latitude": 41.22,
        "sensor_longitude": -73.221,
        "modulation" : 0,
        "encryption" : enctype,
        "meter_distance":100,
        "power" : int(ap.signal),
        "bssid" : ap.address.replace(":",""),
        "essid" : ap.ssid, 
        "channel" : int(ap.channel),
        "apmode" : ap.mode,
        "date_time" : "4-12-2018",
    }

    request = urllib.request.Request(url='http://' + server + '/rf/', data=json.dumps(signal).encode('utf8'), method='PUT', headers={'content-type':'application=json'})
    with urllib.request.urlopen(request) as f:
        pass
    print(f.status)
    print(f.reason)

def scan(interface):
    print("Begin scan")
    wifitree = Cell.all(interface)
    return wifitree

def main(argv):
    #get wifi device from argv
    print ("Arg: " )
    print (argv)
    if (len(argv) == 3):
        interface = argv[1]
        socket = argv[2]
    else:
        interface = 'wlp3s0'
        socket = 'localhost:8888'
    #while(1):    
    #Get GPS Coords
    #perform scan
    #send scan results
    while (1):
        
        sendSignals(socket)
        time.sleep(10) #wait 10 seconds, then rescan

if __name__ == "__main__":
    main(sys.argv)

