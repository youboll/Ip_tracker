import requests
import sys
import json




def location(response):
	print("User's ipv4: ",response['ip'])
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
def track(ip):
	string = "http://api.ipstack.com/"+ str(ip) +"?access_key=8cfdee0b2ee03d45c7f2ccde94cc807d"
	r = requests.get(string)
	reson = r.json()
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
def campo():
	
	#tracking = track(ip)
	class area:
		with open('ips','rb') as reader:
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
