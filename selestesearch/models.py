from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
	company_name = models.CharField(max_length=65, null=True)
	overall_rating = models.CharField(max_length=3)
	culture_values_rating = models.CharField(max_length=3)
	management_rating = models.CharField(max_length=3)
	compensation_benefits_rating = models.CharField(max_length=3)
	opportunities_rating = models.CharField(max_length=3)
	work_life_balance_rating = models.CharField(max_length=3)
	recommend_to_friend_rating = models.CharField(max_length=3)
	
	def __str__(self):
		return self.company_name

class Glassdoor(models.Model):
	company_name = models.ForeignKey('selestesearch.company')
	review_title = models.CharField(max_length=100)
	review_text = models.TextField(max_length=1500)
	overall_rating = models.CharField(max_length=3)
	culture_values_rating = models.CharField(max_length=3)
	management_rating = models.CharField(max_length=3)
	compensation_benefits_rating = models.CharField(max_length=3)
	opportunities_rating = models.CharField(max_length=3)
	work_life_balance_rating = models.CharField(max_length=3)
	recommend_to_friend_rating = models.CharField(max_length=3)

	def __str__(self):
		return self.company_name

class Indeed(models.Model):
	company_name = models.ForeignKey('selestesearch.company')
	review_title = models.CharField(max_length=100)
	review_text = models.TextField(max_length=1500)
	overall_rating = models.CharField(max_length=3)
	culture_values_rating = models.CharField(max_length=3)
	management_rating = models.CharField(max_length=3)
	compensation_benefits_rating = models.CharField(max_length=3)
	opportunities_rating = models.CharField(max_length=3)
	work_life_balance_rating = models.CharField(max_length=3)

	def __str__(self):
		return self.company_name