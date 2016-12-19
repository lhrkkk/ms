#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

from general import gs
log=gs.get_logger(__name__,debug=False)

def test():
    pass


def run(args):
    return True

def selfrun(args={}):
    import vi.init_gs
    from general.interpreter.loader import callrun
    callrun(__file__,args)
if __name__ == '__main__':
    # test()
    selfrun()

