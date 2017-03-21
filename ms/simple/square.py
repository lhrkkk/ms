#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

# 模板
from general import gs
# log=gs.get_logger(__name__)

definition={
    'ensemble_type':'file',
    'action_type':'map',
    'main_function':'square'
}
parameters ={
    'arg1':'1',
    'arg2':'3'
}
#
# definition='''
#     ensemble_type: file,
#     action_type: map
#     main_function: square
#
# '''
#
#
# parameters ={
#     'arg1':'1',
#     'arg2':'3'
# }







def run(element, parameters={}):
    return square(element,parameters)

from vi.interpreter.loaders import call_by_filename
def selfrun(element,args={}):
    import vi.init_gs
    call_by_filename(__file__, element,args)

# 正文

def square(element, args):
    x=element['xyz']
    return x*x


def test():
    pass


# main
if __name__ == '__main__':
    # test()
    selfrun(element={'xyz':2})
