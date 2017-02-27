#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'

from front_face import *


urlpatterns = [
    url(r'^go', views.go_page, name='go'),
    url(r'^view', views.view_page, name='view'),
    url(r'^run', views.run_page, name='run'),
    url(r'^text', views.text_page, name='text'),
]