from django.db import models

# Create your models here.
class Country(models.Model):
	name = models.CharField(null=True, max_length=100)
	iso = models.CharField(null=True, max_length=6)

	def __str__(self):
		return self.name

class State(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
	name = models.CharField(null=True, max_length=100)
	iso = models.CharField(null=True, max_length=6)

	def __str__(self):
		return self.name