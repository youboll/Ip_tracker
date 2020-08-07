from source import *
import argparse
import json

ap = argparse.ArgumentParser()
ap.add_argument('-i','--ip',help="User's ip",dest="ip")
ap = vars(ap.parse_args())
ip = str(ap["ip"])
print("--------------------------Ip tracker------------------\n")
print("Making requests...\n")
if ip != 'None':
	print("Tracking ip...\n\n\n\n")
	tr = track(ip)
	lc = location(tr)
	print("\n\n\nDo you want to export results?(Y/N)")
	res = input(" ")
	if (res == 'Y'or res == 'y'):
		name = "ip_location.json"
		local = "ip_location.txt"
		tr = json.dumps(tr)
		lc = json.dumps(lc)
		ex = output_modular(tr,name,'y')
		lc = output_modular(lc,local,'y')
	else:
		exit()
else:
	print("Scanning ips file...\n")
	tr = campo()