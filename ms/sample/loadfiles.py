#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


from general import gs
log=gs.get_logger(__name__,debug=False)

# print gs.CONF.root_package_name

def test():
    pass

def run(args):
    '''
    读取文件夹内的所有文件夹
    :param args:
    :return:
    '''
    folder=args['folder']


    return True

def selfrun(args={}):
    import vi.init_gs
    from vi.interpreter.loaders import call_by_filename
    call_by_filename(__file__, args)
if __name__ == '__main__':
    # test()
    selfrun()
