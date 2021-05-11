from django.urls import path

from trains.views import *


# Create your tests here:
urlpatterns = [
    # path('', home, name='home'),
    path('', TrainListView.as_view(), name='home'),
    path('add/', TrainCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', TrainDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', TrainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TrainDeleteView.as_view(), name='delete')
]
