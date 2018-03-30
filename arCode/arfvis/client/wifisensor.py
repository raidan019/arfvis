import socket
import sys
from subprocess import call
from wifi import Cell
from pynmea import nmea
import urllib.request
import time
import json

#Client to report wifi data to a Django server using HTTP PUT
def sendSignals(server, wifitree):
    for ap in wifitree:
        encryption = ap.encryption_type
        if (encryption == "None"):
            enctype = 1
        elif (encryption == "wpa"):
            enctype = 2
        elif (encryption == "wpa2"):
            enctype = 3
        elif (encryption == "wep"):
            enctype = 4
        elif (encryption == "opn"):
            enctype = 5
        else:
            enctype = 0 #Default if none of the above
            print ("Warning undefined enc: ", encryption)
        signal = {
            "modulation" : 0,
            "power" : int(ap.signal),
            "bssid" : ap.address.replace(":",""),
            "encryption" : enctype,
            "channel" : int(ap.channel),
            "essid" : ap.ssid,
            "mode" : ap.mode,
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
        socket = 'localhost:8000'
    #while(1):    
    #Get GPS Coords
    #perform scan
    #send scan results
    while (1):
        wifitree = scan('wlp3s0')
        sendSignals(socket, wifitree)
        time.sleep(10) #wait 10 seconds, then rescan

if __name__ == "__main__":
    main(sys.argv)

