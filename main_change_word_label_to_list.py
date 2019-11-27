import os
import re
global label_list
global numberoflabelall
numberoflabelall=0
global hang_number
hang_number=0
global ci_number
ci_number=0
def pipei(copyword,dic,label_list):#匹配函数
    number_of_dic=0
    space=0
    onestr=''
    otherspace=0
    otheronestr=''
    for key,value in dic.items():
        if copyword==key:
            space=0
            for onestr in copyword:
                if onestr==' ':
                    space+=1
            numberofword=space+1
            label_list.append(value)
            numberofword-=1
            while numberofword!=0:
                label_list.append(value+1)
                numberofword-=1
            return 1
    else:
        return 0
    #匹配函数等会再写
    #这里的匹配函数只需要把匹配到的数字串赋值到。。。
    #把label_list做成全局变量？然后在每次标完一个句子以后清空？
def main_change_label_to_list(iter,dic):
    stay=0#当前位置字前一位的编号数，缺省值0
    stayreturn=0#用于记录最后的返回值
    number_of_fit_word=0#本轮进入匹配的词组中的空格数+1
    copyword=""
    i_1=0
    space=0
    #label_list=[]
    first_place=0
    while stay<=len(iter):
        getpipei = 0#确定匹配是否成功，用于跳出
        space=0
        i_1=0
        for wordscan in iter:
            i_1+=1
            if (i_1>stay and wordscan==' '):
                space+=1
        if space>=8:#还有9个词或以上
            number_of_fit_word=8
            i_1=0
            space=0
            for wordscan in iter:
                i_1+=1#第一个字母编号是1不是0
                if i_1>stay and space<8:#这里结束时读取到第八个空格上
                    if wordscan==' ':#读取区间内的空格数计数
                        space+=1
                    if space<8:#不会录入结尾的空格
                        copyword+=wordscan
                if space==8 and first_place==0:
                    stayreturn=i_1#更新stayreturn为读取区间内的第八个空格的位置编号
                    first_place=1
            first_place=0
            if pipei(copyword,dic,label_list):
                stay=stayreturn#8个词直接匹配成功，返回while stay<=len(iter):位置一个stay值继续匹配
                copyword=""
            else:
                copyword=""
                number_of_fit_word=7#匹配不成功的情况下去掉一个空格数（词数）（这里是强赋值）
                while (number_of_fit_word!=0 and getpipei==0):#在还没匹配失败或成功的情况下
                    space=0
                    i_1=0
                    copyword=""
                    for wordscan in iter:
                        i_1+=1
                        if i_1>stay and space<number_of_fit_word:
                            if wordscan==' ':
                                space+=1
                            if space<number_of_fit_word:
                                copyword+=wordscan
                        if space==number_of_fit_word and first_place==0:
                            stayreturn=i_1#更新stayreturn为读取区间内的第number_of_fit_word个空格的位置编号（此处最少为1个空格）
                            first_place=1
                    first_place=0
                    if pipei(copyword,dic,label_list):#匹配到任意词就返回
                        stay=stayreturn
                        getpipei=1
                        copyword = ""
                    else:
                        number_of_fit_word-=1
                if number_of_fit_word==0:
                    label_list.append(9)#没匹配到任何词
                    stay=stayreturn
                    copyword=""

        else :#不到9个词
            pipeichenggong=0
            i_1=0
            copyword=""
            space=0
            first_place1 = 0
            for wordscan in iter:
                i_1+=1
                if i_1>stay:
                    if wordscan==' ':
                        space+=1
                    copyword+=wordscan
                number_of_fit_word=space
            stayreturn=i_1
            number_of_fit_word+=1
            while number_of_fit_word>0 and pipeichenggong==0:
                if pipei(copyword,dic,label_list):
                    number_of_fit_word=0
                    stay=stayreturn
                    pipeichenggong=1
                else:
                    if number_of_fit_word==1:#下面的2－1后由上面匹配还是没成功，到这里说明这个单词已经匹配不到
                        stay=stayreturn
                        number_of_fit_word=0
                        label_list.append(9)
                    if number_of_fit_word>1:
                        copyword=""
                        space=0
                        i_1=0
                        number_of_fit_word-=1
                        for wordscan in iter:
                            i_1+=1
                            if i_1>stay:
                                if wordscan==' ':
                                    space+=1
                                if space<number_of_fit_word:
                                    copyword+=wordscan
                                if space==number_of_fit_word and first_place1==0:
                                    stayreturn=i_1
                                    first_place1=1
                        first_place1=0
            if number_of_fit_word==0:#这里因为number_of_fit_word不再代表空格而是直接代表词，所以当上面number_of_fir_word=1的时候做最后一次单个词的匹配
                stay=stayreturn
                if stayreturn==len(iter):
                    stay+=1
            copyword=""
            number_of_fit_word=0

path1 = "F:/grade/changedata/passage3"
path2 = "F:/grade/changedata/label"
path3 = "F:/grade/changedata/bio"
labelpassage=open(path3+"/labelpassage.txt",'a',encoding='UTF-8')
originalpassage=open(path3+"/originalpassage.txt",'a',encoding='UTF-8')
file1= os.listdir(path1)
label_list_all=[]#用于组建字典前的所有标签数据的数组，此数组数据用于组成字典
for pasage_file_name in file1: #遍历文件夹
    label_list_all = []
    filereallname = os.path.splitext(pasage_file_name)[0]
    if not os.path.isdir(pasage_file_name):
        pasagefile = open(path1 + "/" + pasage_file_name, encoding='UTF-8-sig')
        label_pasagefile = open(path2+"/"+filereallname+"_label.txt",encoding='UTF-8-sig',errors='ignore')
        passage=pasagefile.readlines()#文章
        label=label_pasagefile.readlines()#文章对应的标签
        #读取pasage文件内容和pasage所对应的label文件内容
        pattern1 = re.compile(r'T\d*\sHackingGroup_Name(\s\S+){0,8}$')
        pattern2 = re.compile(r'T\d*\sExploitTarget(\s\S+){0,8}$')
        pattern3 = re.compile(r'T\d*\scountry(\s\S+){0,8}$')
        pattern4 = re.compile(r'T\d*\sLocation(\s\S+){0,8}$')
        pattern5 = re.compile(r'T\d*\sHackingGroup_Name\s\S+\s\S+\s')
        pattern6 = re.compile(r'T\d*\sExploitTarget\s\S+\s\S+\s')
        pattern7 = re.compile(r'T\d*\scountry\s\S+\s\S+\s')
        pattern8 = re.compile(r'T\d*\sLocation\s\S+\s\S+\s')
        for everylabel in label:
            if pattern1.match(everylabel):
                middle_label=re.sub(pattern5,'',everylabel)
                middle_label=middle_label[:-1]
                label_list_all.append(middle_label)
                label_list_all.append(1)
            if pattern2.match(everylabel):
                middle_label=re.sub(pattern6,'',everylabel)
                middle_label = middle_label[:-1]
                label_list_all.append(middle_label)
                label_list_all.append(3)
            if pattern3.match(everylabel):
                middle_label=re.sub(pattern7,'',everylabel)
                middle_label = middle_label[:-1]
                label_list_all.append(middle_label)
                label_list_all.append(3)
            if pattern4.match(everylabel):
                middle_label=re.sub(pattern8,'',everylabel)
                middle_label = middle_label[:-1]
                label_list_all.append(middle_label)
                label_list_all.append(3)
        #print(label_list_all)
        dic = dict(zip(label_list_all[::2], label_list_all[1::2]))#标签对应的字典
        for iter in passage:
            iter=iter[:-1]
            space=0
            if len(iter)>0:
                for i in iter:
                    if i ==' ':
                        space+=1
                if space<80 and iter[0]!=' ' and iter[-1]!=' ':#这里把首尾存在空格的句子删了
                    ci_number+=space
                    label_list=[]
                    main_change_label_to_list(iter,dic)#此函数用来把每句话和词典转换为标注序列(句子长度最长80词，69空格)
                    if len(label_list)==(space+1):
                        #print ('序列与语句词数相同')
                        #print('待标注语句是：',iter)
                        #print('标注序列是：',label_list)
                        changelist=''
                        writin=0
                        for changelabel in label_list:
                            if changelabel!=9:
                                numberoflabelall+=1
                                writin=1
                                print("???")
                            changelist=changelist+str(changelabel)#按字符输入每个label到一行的changelist里头，然后打印到文本
                        if writin==1:
                            hang_number += 1
                            labelpassage.writelines(changelist+'\n')
                            originalpassage.writelines(iter+'\n')
                    else:
                        print('NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                        print (iter)
                        print(label_list)
                    label_list=[]
print("总行数：",hang_number)
print("总词数:",ci_number)
print("总标注数:",numberoflabelall)