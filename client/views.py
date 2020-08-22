from django.shortcuts import render

import urllib.request, json
from .models import Client

def get_client_infos(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	with urllib.request.urlopen("http://ip-api.com/json/"+ip) as url:
		infos = json.loads(url.read().decode())
	infos['agent'] = request.META['HTTP_USER_AGENT']
	infos['host'] = request.META.get('REMOTE_HOST') or request.META.get('HTTP_HOST')
#	infos['host'] = request.META.get('USER')
	client = Client.objects.create(
			query       = infos['query'],
			agent       = infos['agent'],
			host        = infos['host'],
			country     = infos['country'],
			country_code= infos['countryCode'],
			region      = infos['region'],
			region_name = infos['regionName'],
			city        = infos['city'],
			zip_code    = infos['zip'],
			lat         = infos['lat'],
			lon         = infos['lon'],
			timezone    = infos['timezone'],
			isp         = infos['isp'],
			org         = infos['org'],
			ass         = infos['as'],
			url       = request.build_absolute_uri()
		)
	return infos


