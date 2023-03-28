from django.urls import path
from django.contrib.auth import views as auth_views

from .views import base_view, loginPage, registerPage, logoutUser


urlpatterns = [
    path('', base_view, name='home'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutUser, name='logout'),

    #password reset
    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="password_resets/password_reset.html"), 
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="password_resets/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="password_resets/password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="password_resets/password_reset_complete.html"), 
        name="password_reset_complete"),
]