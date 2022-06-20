import json
import os
import random
import numpy as np
from tqdm import *
def readjson():
    path = 'train_bz/'
    output_list=[]
    files=os.listdir(path)
    for file in files:
        f = open(path +'\\' +file ,mode='r',encoding='utf-8')
        dict1 = json.loads(f.read())
        labels_value=dict1.get('labels')
        new_dict=''.join('%s' %a for a in labels_value)
        new_dict=eval(new_dict)
        new_dict['id']=new_dict.pop('name')

        if new_dict.get('id') == '莲雾果':
            new_dict.update({'id':0})
        if new_dict.get('id') == '草莓':
            new_dict.update({'id':1})
        if new_dict.get('id') == '苹果':
            new_dict.update({'id':2})
        if new_dict.get('id') == '红灯笼椒':
            new_dict.update({'id':3})
        if new_dict.get('id') == '易拉盖':
            new_dict.update({'id':4})
        if new_dict.get('id') == '全开盖':
            new_dict.update({'id':5})
        if new_dict.get('id') == '方形蛋糕':
            new_dict.update({'id':6})
        if new_dict.get('id') == '圆形蛋糕':
            new_dict.update({'id':7})
        if new_dict.get('id') == '易撕盖':
            new_dict.update({'id':8})

        id = new_dict.get('id')
        x1=new_dict.get('x1')
        x2=new_dict.get('x2')
        y1=new_dict.get('y1')
        y2=new_dict.get('y2')
        size=new_dict.get('size')
        h=size.get('height')
        w=size.get('width')

        x_ = (x1 + x2) /2/w
        x_ = '%.5f' % x_

        y_ = (y1 + y2) /2/h
        y_ = '%.5f' % y_

        w_ = (x2 - x1) / w
        w_ = '%.5f' % w_

        h_ = (y2 - y1) / h
        h_ = '%.2f' % h_

        for i in range(len(files)):
            continue
        output_list.append([id,x_,y_,w_,h_])
        print(output_list)

    for j in tqdm(output_list):
        output=" ".join(str(x) for x in j)
        f=open('./train.txt','a')
        f.write(output+'\n')
        f.close()

    filename = os.listdir(path)
    filename_ = []
    for i in filename:
        filename_.append(os.path.splitext(i)[0])

    train_txt = open('./train.txt', 'r')
    for j in filename_:
        for line in train_txt.readline():
            f = open('train/{}.txt'.format(j), 'a')
            f.write(line)
            f.close()
    train_txt.close()

readjson()