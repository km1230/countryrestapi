"""countryapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, re_path
from django.contrib import admin
from country import views as cv

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', cv.index, name='index'),
    #path('add_country/', cv.add_country, name='add_country'),
    #path('add_state/', cv.add_state, name='add_state'),
    #path('remove_state/', cv.remove_state, name='remove_state'),
    re_path(r'([\w]{2})/', cv.state_of_country_json, name='find_state'),
]
