#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'urls.py'

__author__ = 'Charles Guo'

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [ 
	url(r'^polls/', include('polls.urls')), 
	url(r'^admin/', admin.site.urls), 
]

