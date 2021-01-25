import requests
import sys
import json
from rich import print



def location(response):
	print("\nUser's ipv4: ",response['ip'])
	print("\n User's country: ",response['country_name'])
	print("\n User's state: ",response['region_name'])
	print("\n User's city: ",response['city'])
	print("\n User's zip code: ",response['zip'])
	print("\n\n Latitude: ",response['latitude'])
	print("\n\n Longitude: ",response['longitude'])
	location = response['location']
	language = location['languages']
	lang = language[0]
	print("\n\n\n Language: ",lang['name'])
	print("\nCountry capital: ",location['capital'])
async def track(ip):
	
	string = "http://api.ipstack.com/"+ str(ip) +"?access_key=8cfdee0b2ee03d45c7f2ccde94cc807d"
	r = requests.get(string)
	reson = r.json()
	setattr(animate,'is_animated',False)
	return(reson)

def output(string,name):
		open_string = 'output'+str(name)+'.json'
		file = open(open_string,'w')
		string = str(string)
		file.write(string)
		return()
def output_modular(string,name,*stri):
	string = str(string)
	export = open(name,'w')
	export.write(string)
	return()

def is_empty(lista):
	if len(lista)==0:
		return('full')
	else:
		return('empty')
def campo(arquivo):
	
	#tracking = track(ip)
	class area:
		with open(str(arquivo),'rb') as reader:
			count = 0
			ips = reader.readlines()
			for x in ips:
				#print(x[-1])

				if (x[-1] == '\n'):
					y = x.replace(x[-1],'')
				else:
					y =x
				json1 = track(y)
				json1 = json.dumps(json1)
				output(json1,count)
				count = count +  1
def espec():
	if(is_empty(sys.argv) != 'empty'):
		ip = sys.argv[1]
	else:
		ip = 'bla'
	track = track(ip)
	local = location(track)
# importing the necessary packages
#If it works remove animation class 
def general_animation(text):
	# This version is fixed and works
	import sys, time
	lowerstr = str(text)
	upperstr = lowerstr.upper()
	for x in range(len(lowerstr)):
	     s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
	     sys.stdout.write(s)
	     sys.stdout.flush()
	     time.sleep(0.1)

async def animate(text,ip):
		import time
		import sys

		
		animation = "|/-\\"
		
		setattr(animate,'is_animated',True)
		colored_string = '[green]   ' + str(text) + '[/green]'
		print(str(colored_string), end = ' ') 
		while(getattr(animate,'is_animated') == True):
			#Gambiara
			for i in range(4):
				time.sleep(0.1)
				sys.stdout.write("\r"+ animation[i % len(animation)])
				sys.stdout.flush()
				res  = await track(ip)

		return(res)
