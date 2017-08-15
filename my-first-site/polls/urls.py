#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'urls.py'

__author__ = 'Charles Guo'

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'), 
]

