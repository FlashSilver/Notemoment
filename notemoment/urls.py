"""iknow URL Configuration

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
from django.conf.urls import include, url,static,patterns
from django.contrib.staticfiles import views
from django.contrib import admin
import settings
from myApp.views import *

urlpatterns = [
        url(r'^qurey/$',query),
        url(r'^send/',create),
        url(r'^file/',file),
        url(r'^postnotes/',postnotes),
        url(r'^getclass/',getclass),
        url(r'^like/',like),
        url(r'^login/',login),
        url(r'^getallclasses/',getallclasses),
        url(r'^saveclass/',saveclass),
        url(r'^getclass/(?P<netid>.*)',getclass),
        url(r'^collect/',collect),
        url(r'^noteinfor/(?P<noteid>.*)',noteinfor),
        url(r'^oneclass/(?P<classname>.*)',oneclass),
        url(r'^history/(?P<netid>.*)',history),
        url(r'^seecollect/(?P<netid>.*)',seecollect),
        url(r'^getcollectfrommobile/(?P<noteid>.*)',getcollectfrommobile),
        url(r'^changeprofile/(?P<content>.*)',changeprofile),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^static/(?P<path>.*)', 'django.views.static.serve', {'document_root': '/Users/zhangtianren/Documents/iknow/static/media/'}),


        #Website
        url(r'^$',home),
        url(r'^weblogin/$',weblogin),
        url(r'^aclass/(?P<classname>.*)',aclass),
         url(r'^upload/$',upload),

]

