#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Meng xiangguo <mxgnene01@gmail.com>
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     |MENG|
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#                        2017/10/3  下午4:19

from django.conf.urls import url
from sign import views_if

urlpatterns = [
    # guest system interface:
    # ex : /api/add_event
    url(r'^add_event', views_if.add_event, name='add_event'),
    # ex : /api/add_guest
    url(r'^add_guest', views_if.add_guest, name='add_guest'),
    # ex : /api/get_event_list
    url(r'^get_event_list', views_if.get_event_list, name='get_event_list'),
    # ex : /api/get_guest_list/
    url(r'^get_guest_list', views_if.get_guest_list, name='get_guest_list'),
    # ex : /api/user_sign/
    url(r'^user_sign', views_if.user_sign, name='user_sign'),
]
