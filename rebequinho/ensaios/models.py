from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class ClinicalTrial(models.Model):
	title = models.CharField(max_length=150)
	tags = models.TextField()
	user_id = models.ForeignKey(User)
	utn_number = models.CharField(max_length=150)
	date_registration_pt = models.DateField()
	scientific_title_pt = models.CharField(max_length=150)
	public_title_pt = models.CharField(max_length=150)
	scientific_title_en = models.CharField(max_length=150)
	public_title_en = models.CharField(max_length=150)
	scientific_title_es = models.CharField(max_length=150)
	public_title_es = models.CharField(max_length=150)
