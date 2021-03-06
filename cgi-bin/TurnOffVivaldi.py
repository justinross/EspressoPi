#!/usr/bin/env python

import sys
import subprocess
import time
import cgitb
cgitb.enable()

# sudo adduser www-data gpio

sys.stdout.write("Content-Type: text/html")
sys.stdout.write("\r\n")
sys.stdout.write("\r\n")

subprocess.check_output(["gpio-admin", "export", "10"])

with open("/sys/devices/virtual/gpio/gpio10/direction","w") as f:
	f.write("out\n");
	
with open("/sys/devices/virtual/gpio/gpio10/value","w") as f:
	f.write("1\n"); # turn on pin

time.sleep(1);

with open("/sys/devices/virtual/gpio/gpio10/value","w") as f:
	f.write("0\n"); # turn off pin

subprocess.check_output(["gpio-admin", "unexport", "10"])

print "Turned off Espresso Machine"
