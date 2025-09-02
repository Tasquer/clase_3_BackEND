from django.urls import path
from . import views
urlpatterns = [
 path("v1/", views.vista1, name="rama1-v1"),
 path("v2/", views.vista2, name="rama1-v2"),
]