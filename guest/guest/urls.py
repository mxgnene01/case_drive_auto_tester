"""guest URL Configuration

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
from sign import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^admin', include(admin.site.urls)),
    url(r'^index$', views.index),
    url(r'^index/$', views.index),
    url(r'^accounts/login/$', views.index),
    url(r'^logout$', views.logout),
    url(r'^login_action$', views.login_action),
    url(r'^event_manage$', views.event_manage),
    url(r'^search_name$', views.search_name),
    url(r'^guest_manage$', views.guest_manage),
    url(r'^search_phone$', views.search_phone),
    url(r'^sign_index/(?P<event_id>[0-9]+)$', views.sign_index),
    url(r'^sign_index_action/(?P<event_id>[0-9]+)$', views.sign_index_action),
    url(r'^api/', include('sign.urls', namespace='sign')),
]
