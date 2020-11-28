from django.db import models

# Create your models here.

class fields(models.Model):
	field_name = models.CharField(max_length=1000)
	value = models.IntegerField(default = 0)


	