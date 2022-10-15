from django.db import models

# Create your models here.

class Link(models.Model):
	name = models.CharField(max_length=80)
	youtube = models.URLField()
	twitter = models.URLField()
	github = models.URLField()
	linkedin = models.URLField()

	def __str__(self):
		return self.name


class Advocate(models.Model):
	name = models.CharField(max_length=80)
	profile_pic = models.URLField(default="")
	short_bio = models.CharField(max_length=50)
	long_bio = models.CharField(max_length=200)
	advocate_since = models.DateField()
	company_name = models.ForeignKey('api.Company', on_delete=models.CASCADE, default="", blank=True)
	links = models.OneToOneField(Link, on_delete=models.CASCADE, default="")
	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

class Company(models.Model):
	company_name = models.CharField(max_length=80)
	company_logo = models.URLField()
	summary = models.CharField(max_length=200)
	advocates_name = models.ManyToManyField(Advocate, blank=True)

	def __str__(self):
		return self.company_name







