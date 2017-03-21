#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : lhr (airhenry@gmail.com)
# @Link    : http://about.me/air.henry

import  re
from general import gs
log=gs.get_logger(__name__,debug=True)

import subprocess

import os
# def gaussian(xyz,code=None,energy_cut=3000000000,database='gaussian',collection='default',method='pm3 ',charge=0,mutiplicity=1,args=None):



def gaussian_calc(file_name,method='pm3 ',charge=0,mutiplicity=1,args=None):

    return "hello this is gaussian."




# def gaussian(conf):
    # xyz=conf['xyz']
    # energy_cut=conf['energy_cut']
    # database=conf['labkit']
    # collection=conf['ensemble']
    # method=conf['method']
    # method=conf['method']
    #
    # charge=0
    # mutiplicity=1


    first_line_re=re.compile(r'^.*?\n.*?\n',re.S)
    txt='#'+method+'\n\n'+'gaussian'+'\n'+first_line_re.sub('\n'+str(charge)+' '+str(mutiplicity)+'\n',xyz+'\n\n')
    print txt

    p=subprocess.Popen(['g09'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    output=p.communicate(input=txt)[0]

    mp2_re=re.compile(r'\\MP2=(.*?)\\',re.S)
    hf_re=re.compile(r'\\HF=(.*?)\\',re.S)
    xyz_re=re.compile(r'Standard orientation:.*?\n -*\n.*? -*\n(.*?) -*\n',re.S)
    # origin_text=out_file.read()
    origin_text=output
    text=origin_text.replace(' ','').replace('\n','')
    mp2_find=mp2_re.findall(text)
    hf_find=hf_re.findall(text)
    xyz_find=xyz_re.findall(origin_text)
    if xyz_find:
        xyzcontent=xyz_find.pop()

    pattern=re.compile(r'[ \t]+.+?[ \t]+(.+?)[ \t]+.+?[ \t]+(.+?)[ \t]+(.+?)[ \t]+?(.+?)\n')
    xyz=pattern.findall(xyzcontent)

    new=[]
    for j,i in enumerate(xyz):
        i=list(i)
        if i[0]=='1':
            i[0]='H'
        elif i[0]=='6':
            i[0]='C'
        elif i[0]=='8':
            i[0]='O'
        elif i[0]=='7':
            i[0]='N'
        elif i[0]=='16':
            i[0]='S'

        new.append(' '.join(i))
    atom_count=len(xyz)

    xyz=str(atom_count)+'\n'+'Energy:\n'+'\n'.join(new)

    if mp2_find:
        hf=float(mp2_find[0])
    else:
        hf=float(hf_find[0])

    xyz= re.sub(r'Energy:', 'Energy:  '+str(hf)+' ',xyz)

    ensemble=Ensemble(db_name=database,collection_name=collection)



    # coll=Conformer.get_coll(database,collection)
    new=Conformer()
    # new.set_coll(database,collection)
    new.loads(xyz)
    new.from_method=method
    new.code=code
    print (new.dumps())

    # 内部可以用Conformer, 因此可以算完了直接入数据库. 另外回调函数可以再执行响应的连接和通知操作.
    # print new.collection
    # 重载save函数, 插入的时候就判重
    # new.save()
    # return True
    # todo: 分离判重复? 以及同时操作数据库的问题, 是否需要设置tryout的次数
    if ensemble.need_conformer(new,energy_cut=energy_cut):
        print '=============='
        ensemble.save(new)
        ensemble_dir=os.path.join(args['work_dir'],args['current_ensemble'])
        log.debug(ensemble_dir)
        # todo: 也许不需要切路径
        origin_dir=os.path.abspath(os.curdir)
        # os.chdir(args['work_dir'])
        try:
            os.mkdir(ensemble_dir)
        except:
            pass


        try:
            os.chdir(ensemble_dir)
            print "------------",ensemble_dir
            if code:
                new.dump(str(code)+'.xyz')
        finally:
            os.chdir(origin_dir)


        # new.save()
    #
    # tryout=0
    # while tryout<5:
    #     try:
    #         new.save()
    #         break
    #     except:
    #         # time.sleep(1)
    #         tryout=tryout+1


    return True
import glob

import beanstalkc
import time

bq = beanstalkc.Connection(host=gs.CONF.beanstalk_server, port=gs.CONF.beanstalk_port)


def gaussian_push(input_folder,output_folder,method):
    '''
    生成推送任务
    :param input_folder:
    :param output_folder:
    :param method:
    :return:
    '''
    filelist=glob.glob(input_folder+"/*.xyz")
    print('jii',filelist)

    all=self.find()

    task={}
    task['module_name']=module_name
    args.update(get_context())
    task['args']=args
    self.bq.use('compute')

    # 取出ensemble所有构型
    # ensemble_name=args['ensemble']
    # 应用单体命令

    for i in all:
        task['args']['xyz']=i['xyz']
        task['args']['code']=i['code']
        task['args']['current_ensemble']=args['current_ensemble']
        print task
        self.bq.put(json.dumps(task))

    # todo: 等待处理完成
    while bq.stats_tube('compute')['current-jobs-ready']!=0 or bq.stats_tube('compute')['current-jobs-reserved']!=0 :
        time.sleep(1)

    # todo: 刷新context
    # context=get_context()
    # context['running_job']
    update_context({'last_ensemble':args['current_ensemble']})



    print input_folder

    return


def run(args):

    return "hello"
    print os.getcwd()

    input_folder=args['input_folder']
    output_folder=args['output_folder']
    method=args['method']

    gaussian_push(input_folder,output_folder,method)

    # gaussian(xyz=xyz,code=code,args=args,energy_cut=energy_cut,database=database,collection=collection,method=method,charge=charge,mutiplicity=mutiplicity)

def test():
    return


def selfrun():
    from vi.interpreter.loaders import call_by_filename
    call_by_filename(__file__)
if __name__ == '__main__':
    # test()

    selfrun()
