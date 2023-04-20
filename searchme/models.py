from django.db import models
from django.contrib.auth.models import User


class adprofile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	utype=models.CharField(max_length=20)
	
class recentlog(models.Model):
	added_by=models.ForeignKey(adprofile, on_delete=models.CASCADE)
	log=models.CharField(max_length=100)


