#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'


class MyDict(dict):
    def __new__(cls, *args, **kwargs):
        self = dict.__new__(cls, *args, **kwargs)
        self.__dict__ = self
        return self