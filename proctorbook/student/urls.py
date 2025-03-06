from django.urls import path
from .views import home
from django.contrib.auth.views import LoginView
from .views import student_signup,signup_page
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView
)
urlpatterns = [
    path('', home, name='home'),
    path('signup/', student_signup, name='student_signup'),
     path('signup/', signup_page, name='signup'),
      path('password_change/', PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
     path('accounts/login/', LoginView.as_view(), name='login'),
]


urlpatterns += [
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
