from django.urls import path
from django.contrib.auth import views as auth_views

from .views import base_view, loginPage, registerPage, logoutUser, change_password


urlpatterns = [
    path('', base_view, name='home'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutUser, name='logout'),
    path('accounts/change-password/', change_password, name='change-password'),

    #email password reset
    path('reset_password/', 
        auth_views.PasswordResetView.as_view(template_name="accounts/pw_reset/password_reset.html", html_email_template_name="accounts/pw_reset/password_reset_html_email.html"), 
        name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="accounts/pw_reset/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="accounts/pw_reset/password_reset_form.html"), 
        name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="accounts/pw_reset/password_reset_complete.html"), 
        name="password_reset_complete"),
]