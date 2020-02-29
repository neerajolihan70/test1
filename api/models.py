from django.db import models

class ApiModel(models.Model):

	name = models.CharField(max_length=50)
	email = models.EmailField()
	mobile = models.BigIntegerField()
	movie = models.CharField(max_length=30)
	class Meta:
		db_table = 'api'