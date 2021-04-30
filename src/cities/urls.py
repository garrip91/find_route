from django.urls import path

from cities.views import *



# Create your tests here:
urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
]