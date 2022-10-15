from rest_framework import serializers
from .models import Advocate, Company, Link


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		ordering = ['-id']
		model = Company
		fields = ("company_name", "company_logo", "summary")


class LinkSerializer(serializers.ModelSerializer):
	class Meta:
		ordering = ['-id']
		model = Link
		fields = ("youtube", "twitter", "github", "linkedin")

class AdvocateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Advocate
		fields = "__all__"
		depth = 1