from django.urls import path
from . import views
urlpatterns = [
 path("v1/", views.vista1, name="rama2-v1"),
 path("v2/", views.vista2, name="rama2-v2"),
]
