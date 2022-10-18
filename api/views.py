from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer
from rest_framework import viewsets

class AdvocatesViewSet(viewsets.ModelViewSet):
	serializer_class = AdvocateSerializer

	def get_queryset(self):
		advocate = Advocate.objects.all()
		return advocate


	def retrieve(self, request, pk):
		advocate = Advocate.objects.filter(id=pk)
		ser = AdvocateSerializer(advocate[0])
		return Response(ser.data)

class CompanyViewSet(viewsets.ModelViewSet):
	serializer_class = CompanySerializer

	def get_queryset(self):
		company = Company.objects.all()
		return company