import os
import re
import nltk
from nltk.tokenize import sent_tokenize
path1 = "F:/grade/changedata/cleandatalast"
path2 = "F:/grade/changedata/cleandatarealylast"
files= os.listdir(path1)
pattern1=re.compile(r'^Release_URL')
pattern2=re.compile(r'^Report_URL')
pattern3=re.compile(r'^Release_Time')
for file in files: #遍历文件夹
     filereallname=os.path.splitext(file)[0]
     aentence = ""
     passage=[]
     if not os.path.isdir(file):
         f = open(path1 + "/" + file, encoding='UTF-8')
         filewrite = open(path2 + "/" + file,'a',encoding='UTF-8')
         all_sentence=""
         for sentence in f.readlines():
             all_sentence=all_sentence+sentence
         printpasage=sent_tokenize(all_sentence)
         print(printpasage)
         for i in printpasage:
            longrange=len(i)
            print(i)
            print(longrange)
            k=0
            space=0
            for j in i:
                if k<longrange-1:
                    if j==' ':
                        space+=1
                    if j!=' ':
                        space=0
                    if space<=1:
                        filewrite.write(j)
                else :
                    filewrite.write('\n')
                k+=1
