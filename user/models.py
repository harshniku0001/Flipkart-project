from django.db import models

class loginuser(models.Model):
	fname=models.CharField(max_length=20)
	lname=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	email=models.CharField(max_length=20)
	confirm_password=models.CharField(max_length=20)
	username=models.CharField(max_length=20)


	
