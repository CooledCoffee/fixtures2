# -*- coding: utf-8 -*-

def generate_raise_func(error):
    def _func(*args, **kw): # pylint: disable=unused-argument
        raise error
    return _func
