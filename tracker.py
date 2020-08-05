import requests
import sys

ip = sys.argv[1]
def track(ip):
	string = "http://api.ipstack.com/"+ str(ip) +"?access_key=8cfdee0b2ee03d45c7f2ccde94cc807d"
	r = requests.get(string)
	reson = r.json()
	def location(response):
		print("User's ipv4: ",reson['ip'])
		print("\n User's country: ",reson['country_name'])
		print("\n User's state: ",reson['region_name'])
		print("\n User's city: ",reson['city'])
		print("\n User's zip code: ",reson['zip'])
		print("\n\n Latitude: ",reson['latitude'])
		print("\n\n Longitude: ",reson['longitude'])
		location = reson['location']
		language = location['languages']
		lang = language[0]
		print("\n\n\n Language: ",lang['name'])
	l = location(reson)

tracking = track(ip)