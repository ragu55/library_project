from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="book"),
    path('listings', views.listings, name="listings"),
    path('<int:id>/listing', views.listing, name="listing"),
]
