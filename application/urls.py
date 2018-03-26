"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views

from comments import views as comments_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('add_comments/', comments_views.add_comments, name='add_comments'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        accounts_views.activate, name='activate'),
    path('confirm/', TemplateView.as_view(template_name='confirm_email.html'), name='confirm'),
    path('confirm/done', auth_views.LoginView.as_view(template_name='confirm_done.html'), name='confirm_done'),
    path('confirm/fail', TemplateView.as_view(template_name='confirm_fail.html'), name='confirm_fail'),

    # url for ajax
    path('load_comments/', comments_views.load_comments, name='load_comments'),
]
