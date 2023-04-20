from django.db import models

# Create your models here.
class pdfsmodels(models.Model):
	name=models.CharField(max_length=20)
	details=models.CharField(max_length=500)
	rating=models.CharField(max_length=12)
	file=models.FileField(upload_to='file')