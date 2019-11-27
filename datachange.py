import os
import re
import nltk
from nltk.tokenize import sent_tokenize
path1 = "F:/grade/changedata/cleandatafirst"
path2 = "F:/grade/changedata/cleandatalast"
files= os.listdir(path1)
pattern1=re.compile(r'^Release_URL')
pattern2=re.compile(r'^Report_URL')
pattern3=re.compile(r'^Release_Time')
pattern4=re.compile(r'\(')
pattern5=re.compile(r'\)')
for file in files: #遍历文件夹
     filereallname=os.path.splitext(file)[0]
     iter_f = ""
     passage=[]
     if not os.path.isdir(file):
         f = open(path1 + "/" + file, encoding='UTF-8')
         filewrite = open(path2 + "/" + file,'a',encoding='UTF-8')
         for iter_f in f.readlines():
            match1 = pattern1.match(iter_f)
            match2 = pattern2.match(iter_f)
            match3 = pattern3.match(iter_f)
            if not match1 and not match2 and not match3:
                for i in iter_f:
                    if i!=','and i!='“'and i!='?'and i!='”'and i!='•' and i!='\n' and i!='\t' and i!='（'and i!='）'and i!='‘'and i!='’'and i!='■' and i!='[' and i!=']' and i!='('and i!=')':
                        filewrite.writelines(i)
                    if i=='”'or i=='\n'or i=='\t':
                        filewrite.writelines(' ')
                    if i=='\"':
                        filewrite.writelines(' \" ')
                    if i==',':
                        filewrite.writelines(' ,')
                    if i=='‘'or i=='’':
                        filewrite.writelines(' ')
                    if i=='（'or i=='(':
                        filewrite.writelines('( ')
                    if i=='）'or i==')':
                        filewrite.writelines(' )')


filewrite.close()