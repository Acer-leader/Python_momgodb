#!/usr/bin/python
#coding=utf-8
#Author:Lun.Chen
#Version:Python3.6
#Tools :Pycharm 2017.1.2
def  menu():
    print('''菜单列表：
        1-->S:返回上一级
        2-->M:返回首页菜单
        3-->查找下一级行政单位请输入名称
        4-->Q:退出系统'''
    )
def province_one():
    file = open("province.txt", 'r', encoding='UTF-8')
    readlines = file.readlines()
    provice = []
    for line in readlines:
        line = line.strip('\n')
        provice.append(line.spl)
    province = sorted(set(provice), key=provice.index)
    row=1
    print('省级菜单：')
    for data in province:
        print('  ',row,data)
        row+=1
    menu()
    promit=input("请选择操作:")
    if promit=='S':
        __main__()
    elif promit == 'Q':
        print("系统退出！")
    else:
        city(promit)
def city(provinceName):
    file = open("province.txt", 'r', encoding='UTF-8')
    readlines = file.readlines()
    city = []
    for line in readlines:
        line = line.strip('\n')
        if line.split('\t')[0]==provinceName:
            city.append(line.split('\t')[1])
    city = sorted(set(city), key=city.index)
    row = 1
    print('市级菜单：')
    for data in city:
        print('  ', row, data)
        row += 1
    menu()
    promit = input("请选择操作:")
    if promit == 'S':
        province_one()
    elif promit == 'Q':
        print("系统退出！")
    else:
        area(provinceName,promit)
def area(provinceName,cityName):
    file = open("province.txt", 'r', encoding='UTF-8')
    readlines = file.readlines()
    area = []
    for line in readlines:
        line = line.strip('\n')
        if line.split('\t')[0] == provinceName and line.split('\t')[1] == cityName:
            area.append(line.split('\t')[2])
        area = sorted(set(area), key=area.index)
    row = 1
    print('区级菜单：')
    for data in area:
        print('  ', row, data)
        row += 1
    menu()
    promit = input("请选择操作:")
    if promit == 'S':
        city(provinceName)
    elif promit == 'Q':
        print("系统退出！")
    else:
        print('输入无效!')
if __name__=="__main__":
    menu()
    runever=True
    while runever:
        promit = input("请选择操作(A:查找所有省份,Q:退出系统")
        if promit == 'A':
            province_one()
        elif promit == 'Q':
            print("系统退出！")
            runever=False
        else:
            print('请输入有效信息：')