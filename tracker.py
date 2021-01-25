from source import *
import argparse
import json
import asyncio
from rich import print
ap = argparse.ArgumentParser()
ap.add_argument('-i','--ip',help="User's ip",dest="ip")
ap = vars(ap.parse_args())
ip = str(ap["ip"])
#Works with command line arguements and by itself
print(len(ip))
if (len(ip) == 4):
	ip = input("Ip to be tracked: ")
	if (ip.count('.')  < 1):
		tr = campo(ip)

print("[purple]--------------------------[/purple][blue]Ip tracker[/blue][purple]------------------[/purple]\n")
print("\n[bold red italic]Making requests...[/bold red italic]\n")
if len(ip) != 4:
	#print("Tracking ip...\n\n\n\n")
	#x = animation("Tracking ip")
	
	#await animate("Tracking ip")
	#x.stop_anime()
	#tr = animate(ip)
	tr = asyncio.run(animate("Tracking Ip",ip))
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