#!/usr/bin/env python
# -*- coding: utf-8 -*-


def story(**kwds):
    return 'Once upon a time, there was a ' \
           '%(job)s called %(name)s' % kwds


def power(x, y, *others):
    if others:
        print 'Received redundant parameters:', others
    return pow(x, y)


def interval(start, stop=None, step=1):
    """Imitates range() for step > 0"""
    if stop is None:
        start, stop = 0, start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

print story(job='King', name='Gumby')
print story(name='Skyler', job='coder')
params = {'job': 'teacher', 'name': 'Li'}
print story(**params)
