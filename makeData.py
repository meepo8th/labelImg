import os
import random

trainval_percent = 0.66
train_percent = 0.5
xmlfilepath = 'E:/picRecord/data_plus/data/VOC2012/Annotations'
txtsavepath = 'E:\picRecord\data_plus\data\VOC2012\ImageSets\Main'
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

ftrainval = open('E:\picRecord\data_plus\data\VOC2012\ImageSets/Main/trainval.txt', 'w')
ftest = open('E:\picRecord\data_plus\data\VOC2012\ImageSets/Main/test.txt', 'w')
ftrain = open('E:\picRecord\data_plus\data\VOC2012\ImageSets/Main/train.txt', 'w')
fval = open('E:\picRecord\data_plus\data\VOC2012\ImageSets/Main/val.txt', 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()