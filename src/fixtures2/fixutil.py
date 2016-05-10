# -*- coding: utf-8 -*-

def generate_raise_func(error):
    def _func(*args, **kw):
        raise error
    return _func
