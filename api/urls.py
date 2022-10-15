from django.urls import path, include
from . import views

from .views import AdvocatesViewSet, CompanyViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r"advocates", AdvocatesViewSet, basename="advocates")
router.register(r"companies", CompanyViewSet, basename="companies")

urlpatterns = [
	# path('', views.getData)
	path("", include(router.urls))
]