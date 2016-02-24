from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# glassdoor: CEO/numberOfRatings; Indeed scrape


class Review(models.Model):
	username = models.ForeignKey('auth.User')
	company_name = models.CharField(max_length=50)
	review_title = models.CharField(max_length=60)
	review_text = models.TextField(max_length=1500)
	overall_rating = models.CharField(max_length=1)
	culture_values_rating = models.CharField(max_length=1)
	management_rating = models.CharField(max_length=1)
	compensation_benefits_rating = models.CharField(max_length=1)
	opportunities_rating = models.CharField(max_length=1)
	work_life_balance_rating = models.CharField(max_length=1)
	recommend_to_friend_rating = models.CharField(max_length=1)
	review_date = models.DateTimeField(blank=True, null=True)

	def save_review(self):
		self.review_date = timezone.now()
		self.save()

	def __str__(self):
		return self.review_title
