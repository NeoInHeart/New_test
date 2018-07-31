# -*- coding: utf-8 -*-
#Auther :Liang Qiang
#一般的求素数的方法(for循环版)时间：0.031001806259155273
from math import sqrt
import time
startime=time.time()
series=[]
for i in range(2,100001):
    flag=1
    k=int(sqrt(i))
    for a in range(2,k+1):
        if i%a==0:
            flag=0
            break
    if(flag):
      series.append(i)
print(len(series))
endtime=time.time()
print(endtime-startime)

#while循环版 时间：0.049002647399902344
startime1=time.time()
series1=[]
j=2
while(j<=100000):
    i=2
    k=int(sqrt(j))
    while(i<=k):
        if j%i==0:break
        i+=1
    if(i>k):
        series1.append(j)
    j+=1
print(len(series1))
endtime1=time.time()
print(endtime1-startime1)


#提升速度的求素数的方法1 时间：0.054003238677978516
startime2=time.time()
series2=[]
for i in range(2,100001):
    flag=1
    k=int(sqrt(i))
    if(i==2 or i==3):
        series2.append(i)
        continue
    if i%2==0:
        continue
    else:
        for a in [x for x in range(3,k+1) if x % 2 != 0]:
            if i%a==0:
                flag=0
                break
        if(flag):
            series2.append(i)
print(len(series2))
print(time.time()-startime2)

