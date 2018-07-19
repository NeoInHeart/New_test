# -*- coding: utf-8 -*-
#Auther :Liang Qiang
import re
a="1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 ))- (-4*3)/(16-3*2))"
#输入的字符串直接计算乘除法
def multiply_divide(str):
    calc=re.split("[*/]",str)
    print(calc)
    op=re.findall("[*/]",str)
    ret=None
    for index,i in enumerate(calc):
        if ret:
            if op[index-1]=="*":
                ret*=float(i)
            elif op[index-1]=="/":
                ret/=float(i)
        else:
            ret=float(i)
    return ret
#对输入的字符串直接计算加减
def add_sub(split_,find_):
    res=None
    for index,i in enumerate(split_):
        if res:
            print(find_[index-1])
            if find_[index-1]=='+':
                res+=float(i)
            elif find_[index-1]=='-':
                res-=float(i)

        else:
            res=float(i)
    return str(res)
#去除多余符号
def del_double(str):
    str = str.replace("++", "+")
    str = str.replace("--", "-")
    str = str.replace("+-","-")
    str = str.replace("- -","-")
    str = str.replace("+ +","+")
    return str
#处理函数
def calcul_contrl(str):
    str=str.strip("()")
    str = del_double(str)
    print(str)
    find_=re.findall("[+-]",str)
    split_=re.split("[+-]",str)
    if len(split_[0].strip()) == 0:  # 特殊处理
        split_[1] = find_[0] + split_[1] # 处理第一个数字前有“－”的情况，得到新的带符号的数字
         # 处理第一个数字前为负数“-"，时的情况，可能后面的操作符为“－”则进行标记
        if len(split_) == 3 and len(find_) ==2:
            tag =True
            del split_[0] # 删除原分割数字
            del find_[0]
        else:
            del split_[0] # 删除原分割数字
            del find_[0]  # 删除原分割运算符
    print(split_,find_)
    for index, i in enumerate(split_):
         # 去除以*或/结尾的运算数字
        if i.endswith("* ") or i.endswith("/ "):
            split_[index] = split_[index] + find_[index] + split_[index+1]
            del split_[index+1]
            del find_[index]
    for index, i in enumerate(split_):
        if re.search("[*/]",i): # 先计算含*/的公式
            sub_res = multiply_divide(i) #调用剩除函数
            split_[index] = sub_res
            print(sub_res)
    print(split_,find_)
    return add_sub(split_,find_)

if __name__=='__main__':
    cacl_input=input("请输入计算公式，默认为%s:"%a).strip()
    if len(cacl_input)==0:
        cacl_input=a
    cacl_input=r"%s"%cacl_input
    print("直接用eavl()计算的结果为：%s"%eval(cacl_input))
    flag=True
    result=None
    while flag:
        inner=re.search("\([^()]*\)",cacl_input)
        if inner:
            b=inner.group()
            print("需要计算的公式%s"%b)
            c=calcul_contrl(b)
            print("计算后的结果：%s"%c)
            cacl_input=cacl_input.replace(str(inner.group()), c)

            print(cacl_input)
            print("处理括号内的运算[%s]结果是：%s" % (inner.group(),str(c)))

        else:
            d=calcul_contrl(cacl_input)
            result=d
            print("采用本程序计算结果为：%s"%d)
            flag = False
