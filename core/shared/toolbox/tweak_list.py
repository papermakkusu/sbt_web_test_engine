#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'MGVasilev'


def has_elem(li):
    try:
        next(iter(li))
        return True
    except StopIteration:
        return False


def calc_max(li):
    if len(li) > 0:
        return len(li) - 1
    return


def first(li):
    if len(li) > 0:
        return li[0]
    return None


def last(li):
    if len(li) > 0:
        return li[-1]
    return None


def first_or_empty(li):
    if len(li) > 0:
        return li[0]
    return b""

