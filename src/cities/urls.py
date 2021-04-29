from django.urls import path

from cities.views import *



# Create your tests here:
urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/', home, name='home'),
]