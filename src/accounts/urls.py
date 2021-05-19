from django.urls import path

from accounts.views import registration_view, login_view, logout_view


# Create your paths here:
urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
