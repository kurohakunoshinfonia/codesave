import os
import re
import nltk
from nltk.tokenize import sent_tokenize
path = "F:/grade/changedata/database3"
files= os.listdir(path)
long=[0 for i in range(14)]
all=0
zero_or_one=0
longofsentence=0
maxmum=0
oneofrange=1
for file in files: #遍历文件夹
     filereallname=os.path.splitext(file)[0]
     passage=[]
     if not os.path.isdir(file):
         f = open(path + "/" + file, encoding='UTF-8')
         for sentence in f.readlines():
            longofsentence=1
            all+=1
            for i in sentence:
                if i==' ':
                    longofsentence+=1
            oneofrange=1
            for i in range(0,14):
                if longofsentence<(oneofrange+5) and longofsentence>=oneofrange:
                    long[i]+=1
                oneofrange+=5
            oneofrange=1
print(long)
for i in range(0,14):
    maxmum+=long[i]
print(maxmum)
print(all)
#长度取70