#coding=utf-8
"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include('restapi.urls')),
]


from restapi.decorators import api





import re

pattern = re.compile('^[1][358][0-9]{9}$') 


@api
def check_phone(phone_number):
    from django.contrib.auth.models import User
    print User.objects.all()
    # return True if pattern.match(phone_number) else False
    return True if re.match('^[1][358][0-9]{9}$', phone_number) else False


@api
def hello(world='world'):
    """
    hello <wolrd>
    """
    return 'hello %s' % world


@api(types = {'a': float, 'b': float})
def calc(a, b):
    """
    + - * /
    """
    return {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a / b
    }
