from django.urls import path
from . import views

urlpatterns = [
    path('', views.details, name="author_details")
]