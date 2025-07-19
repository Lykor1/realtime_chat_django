from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.chat_page, name='chat_page'),
    path('auth/login/', LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]
