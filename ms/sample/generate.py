#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

from general import gs
log=gs.get_logger(__name__,debug=False)

from vi.scheduler.push import push_compute

# def push_decoding(code):

from ms.conformer import Conformer
from general.interpreter.context import update_context

def push_generate(args):
    origin=Conformer()
    for i in origin.generate():
        print i
        args['xyz']=Conformer().decoding(i).to_xyz()
        push_compute('compute.gaussian',args)

from vi.ensemble.ensemble import Ensemble

def ensemble_generate(args):
    # origin=Conformer()
    args['current_ensemble']=args['ensemble_name']+'_sample_generate'
    update_context({'last_ensemble':args['current_ensemble']})

    codes=Conformer().generate()
    for i in codes:
        args['code']=i
        # push_compute("conformer.decode",args)

        conformer= Conformer().decoding(args['code'])
        ensemble=Ensemble(collection_name=args['current_ensemble'])
        ensemble.save(conformer)

        # conformer= Conformer().decoding(i)
        # ensemble=Ensemble(collection_name=args['current_ensemble'])
        # ensemble.sagaussian',args)






def run(args):
    # push_generate(args)
    ensemble_generate(args)
    return True


def selfrun(args={}):
    from general.interpreter.loader import callrun
    callrun(__file__,args)
if __name__ == '__main__':
    # test()
    selfrun()


