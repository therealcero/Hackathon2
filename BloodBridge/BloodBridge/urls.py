"""
URL configuration for BloodBridge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('bank_home/', views.bank_home, name='bank_home'),
    path('bank_home/find', views.find, name='find'),
    path('find', views.find, name='find'),
    path('search_donors/', views.search_donors, name='search_donors'),
    path('donor_home/', views.donor_home, name='donor_home')
]
