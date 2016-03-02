from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from selestesearch.models import Company, Glassdoor, Indeed, Seleste

class CompanySerializer(serializers.ModelSerializer):
	