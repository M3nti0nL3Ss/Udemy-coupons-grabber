from django.db import models


class Client(models.Model):
	query        = models.CharField(max_length=100,blank=True)
	agent        = models.CharField(max_length=500,blank=True)
	country      = models.CharField(max_length=200,blank=True)
	country_code = models.CharField(max_length=100,blank=True)
	region       = models.CharField(max_length=100,blank=True)
	region_name  = models.CharField(max_length=100,blank=True)
	city         = models.CharField(max_length=100,blank=True)
	zip_code     = models.CharField(max_length=100,blank=True)
	lat          = models.CharField(max_length=100,blank=True)
	lon          = models.CharField(max_length=100,blank=True)
	timezone     = models.CharField(max_length=100,blank=True)
	isp          = models.CharField(max_length=100,blank=True)
	org          = models.CharField(max_length=100,blank=True)
	ass          = models.CharField(max_length=100,blank=True)
	host         = models.CharField(max_length=200,blank=True)
	date         = models.DateTimeField(auto_now_add=True)
	url          = models.CharField(max_length=100,blank=True,default='none')
	def __str__(self):
		return self.query
