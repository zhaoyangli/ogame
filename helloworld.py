# -*- coding: utf-8 -*-
from random import randint
# import turtle
# turtle.Turtle.forward(11)
# import gitlab
# lines =['pwer;usdf;lier;sdfdsf;group','eeee;uuuu;iiiii;lllll;project']
#
# for _ in lines:
#     line = _.split(';')
#     print (line)
#     if line[4]  == 'group':
#         line[1] = ''
#     del line[4]
#
#     if line[1]:
#         line1 = ';'.join(i for i in line)
#
#         print (line1)

import requests
import xml.etree.ElementTree as ET
def is_noob(id):
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/highscore.xml?category=1&type=1')
    root = ET.fromstring(req.content)
    for child in root:
        try:
            if id == child.attrib['id']:
                return int(child.attrib['score']) <= 44000
        except Exception as e:
            print(e)
            return True

def find_I():
    '''
    :return: list of I planet
    '''
    Iplayer = []
    results = []
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/players.xml')
    root = ET.fromstring(req.content)
    for child in root:
        try:
            sta = child.attrib['status']
        except:
            sta = 'normal'
        if sta == 'I' and not is_noob(child.attrib['id']):
            Iplayer.append(child.attrib['id'])
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/universe.xml')
    # print(req.content)
    root = ET.fromstring(req.content)
    for child in root:
        if child.attrib['player'] in Iplayer:
            # print(child.tag, child.attrib)
            results.append(child.attrib['coords'])
    return results

def find_i():
    '''
    :return: list of i planet
    '''
    Iplayer = []
    results = []
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/players.xml')
    root = ET.fromstring(req.content)
    for child in root:
        try:
            sta = child.attrib['status']
        except:
            sta = 'normal'
        if sta == 'i' and not is_noob(child.attrib['id']):
            Iplayer.append(child.attrib['id'])
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/universe.xml')
    # print(req.content)
    root = ET.fromstring(req.content)
    for child in root:
        if child.attrib['player'] in Iplayer:
            # print(child.tag, child.attrib)
            results.append(child.attrib['coords'])
    return results

def find_i_player():
    '''
    :return: list of i planet
    '''
    Iplayer = []
    results = []
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/players.xml')
    root = ET.fromstring(req.content)
    for child in root:
        try:
            sta = child.attrib['status']
        except:
            sta = 'normal'
        if sta == 'i' and not is_noob(child.attrib['id']):
            Iplayer.append(child.attrib['id'])
    req = requests.get('https://s101-jp.ogame.gameforge.com/api/universe.xml')
    # print(req.content)
    root = ET.fromstring(req.content)
    for player in Iplayer:
        for child in root:
            if child.attrib['player'] == player:
                # print(child.tag, child.attrib)
                results.append(child.attrib['coords'])
                break
    return results

print(find_i_player())

def write_to_text():
    pass

from time import sleep
# import random
# def delay_r(int_default):
#     # sleep(int_default)
#     # sleep(random.random()*int_default)
#     print(random.random()*int_default)
# delay_r(2)

import urllib.request
import json

# from city import city

# exit = False

# while not exit:
#     cityname = input("你想查询哪个城市的天气？输入q退出\n")
#     if cityname == "q" or cityname == "Q":
#         print("退出！")
#         exit = True
#     else:
#         # citycode=city.get(cityname)
#         citycode = 101010100
#         if citycode:
#             url = ("http://www.weather.com.cn/data/cityinfo/%s.html" % citycode)
#             # url = ("http://www.sojson.com/open/api/weather/json.shtml?city=%s" % cityname)
#
#             # url = ("http://www.sojson.com/open/api/weather/json.shtml?city=北京")
#             request = urllib.request.Request(url)
#             response = urllib.request.urlopen(request)
#             content = response.read().decode("utf-8")
#             print(content)
#             data = json.loads(content)
#             print(data)
#             print(type(content))
#             print(type(data))
#
# class Vehicle:
#     def __init__(self, speed):
#         self.speed = speed
#
#     def drive(self, distance):
#         print ("need %f hour(s)" % (distance / self.speed))
#
# class Bike(Vehicle):
#     pass
#
# class Car(Vehicle):
#     def __init__(self, speed, fuel):
#         Vehicle.__init__(self, speed)
#         self.fuel = fuel
#
#     def drive(self, distance):
#         Vehicle.drive(self, distance)
#         print ('need %f fuels' % (distance * self.fuel))
#
# b = Bike(15.0)
# c = Car(80.0, 0.012)
# b.drive(100.0)
# c.drive(100.0)


# score = {
#      '萧峰': 95,
#      '段誉': 97,
#      '虚竹': 89
# }
#
# for name in score:
#     print(score[name])
#
# print (score)


# i = 0
# while i < 5:
#    i += 1
#    for j in range(3):
#        print (j)
#        if j == 2:
#            break
#    for k in range(3):
#        if k == 2:
#            continue
#        print (k)
#    if i > 3:
#        break
#    print (i)

# f = open('data.txt','w')
# f.write('a string you want to write')
# data = f.readlines()
# print (data)
#
# f.close()


# s = ' '
# li = ['apple', 'pear', 'orange']
# fruit = s.join(li)
# print (fruit)
# for c in fruit:
#    print (c,end='')

# list = [1,2,3,5]
# print (list)
# print (list[1])
# list[2] = 4
# list.append('us')
# print (list)
# print (list[1:3])
#
# def sayHello(someone):
#     print (someone + 'hello world!')
#
# for i in list:
#     sayHello( str(i) + ' hi ')
#
# for i in range(2,4):
#     sayHello( str(i) + ' hi ')


# sayHello('hi ')


# bool(-123)
# bool(0)
# bool('abc')
# bool('False')
# bool('')
# print(bool(0))

# for i in range(0, 5):
#    for j in range(0, 5):
#        print ('*',end="")
#    print()

# for i in range(0, 5):
#    print('*', end=' ')

# num = 18
# print ('My age is %d %d' %(num,num) )
# num = 18
# print ('My age is %d' %num,"%d" %num )

# print('''safas\n
# adfsadf''')

# a=0
# number=0
# while number < 100:
#     number+=1
#     a += number
# print(a)

# a=0
# for i in range(1, 101):
#    a+=i
# print(a)


# a = True
# b = not a  #不记得not请回复6
# # 想想下面这些逻辑运算的结果，然后用print看看你想的对不对：
# print(b,not b,
# a == b,
# a != b
# ,a or b,
# 1<2 and b==True)
# not b
# a == b
# a != b
# a and b
# a or b
# 1<2 and b==True

# a = 1  # 先a设为1
# while a != 0:  # a不等于0就一直做
#     print(
#     "please input")
#     a = int(input())
# print(
# "over")


# thisIsLove = input()
# if thisIsLove == "True":
#     print("再转身就该勇敢留下来")


# num = 10
# print('Guess what I think?')
#
# answer = int(input())
# if answer < num:
#     print('too small!')
#
# if answer > num:
#     print(
#     'too big!')
# if answer == num:
#     print(
#     'BINGO!')
