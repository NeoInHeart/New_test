# -*- coding: utf-8 -*-
# author: liangQiang

import time

def search():
    f=open("practise","r",encoding="utf-8")
    TheSearch=str(input("请输入需要查询的信息："))
    i=0
    for line in f:
         line=line.strip()
         if TheSearch in line or i==0:
              continue
    return line
    f.close()

def add():
    f=open("practise","r",encoding="utf-8")
    for line in f:
         line=line.strip()
         if "123" in line:
              line = line.replace("123","Liang Qiangqiang is the hero ")

    f.close()

def update():
    f=open("practise","r",encoding="utf-8")
    for line in f:
         line=line.strip()
         if "123" in line:
              line = line.replace("123","Liang Qiangqiang is the hero ")

    f.close()

def delete():
    f=open("practise","r",encoding="utf-8")
    for line in f:
         line=line.strip()
         if "123" in line:
              line = line.replace("123","Liang Qiangqiang is the hero ")

    f.close()



print('''
 1.search
 2.add
 3.update
 4.delete
''')
selected=int(input("请输入你的选择序号："))
if selected==1:
    print(search())
elif selected==2:
    add()
elif selected==3:
    update()
elif selected==4:
    delete()
else:
    exit()






