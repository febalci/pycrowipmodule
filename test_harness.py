#!/usr/bin/env python3
import signal
import sys
from pycrowipmodule import CrowIPAlarmPanel

#This is a test harness for the pycrowipmodule library.

#Please Enter Own Details:
ip = '192.168.1.11'
port = '5002'
code = '0000'

na = input("Config complete. Please press enter now to connect to the Crow/AAP IP Module.  When finished, use Ctrl+C to disconnect and exit")
testpanel = CrowIPAlarmPanel(ip, int(port), code)
testpanel.start()

def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        testpanel.stop()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.pause()
