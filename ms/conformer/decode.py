#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry


from general import gs
log=gs.get_logger(__name__,debug=False)

from ms.conformer import Conformer
from vi.ensemble_mongo.ensemble import Ensemble

def test():
    pass


def run(args):
    conformer= Conformer().decoding(args['code'])
    ensemble=Ensemble(collection_name=args['current_ensemble'])
    ensemble.save(conformer)

    return True

def selfrun(args={}):
    from vi.interpreter.loaders import call_by_filename
    call_by_filename(__file__, args)
if __name__ == '__main__':
    # test()
    selfrun()


