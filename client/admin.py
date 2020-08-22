from django.contrib import admin
from .models import Client

class Clientt(admin.ModelAdmin):
	list_display = ['host','query','country','city','date']
	list_filter = ['host','date']
	readonly_fields = ["query",
	"agent",       
	"country",     
	"country_code",
	"region",      
	"region_name", 
	"city",        
	"zip_code",    
	"lat",         
	"lon",         
	"timezone",    
	"isp",         
	"org",         
	"ass",         
	"date",
	"host",
	"url",     
	]
	search_fields = ['country','country_code']
admin.site.register(Client,Clientt)

