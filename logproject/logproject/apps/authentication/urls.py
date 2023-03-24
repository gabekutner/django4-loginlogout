from django.urls import path
from .views import base_view, loginPage, registerPage, logoutUser

urlpatterns = [
    path('', base_view, name='home'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutUser, name='logout'),
]