
import pandas as pd
import csv
import re
import string

usatemperature  = open('usa.csv', 'rb')
reader = csv.reader(usatemperature)

fullyear =[]
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g=0
h=0
j=0
k=0
l=0
m=0
n=0
o=0
st = ['/00', '/01', '/02', '/03', '/04', '/05', '/06', '/07', '/08', '/09', '/10',
 '/11', '/12', '/13', '/14', '/15', '/16', '/17', '/18',
 '/19', '/20', '/21', '/22', '/23', '/24', '/25', '/26', '/27', '/28', '/29',
 '/30', '/31', '/32', '/33', '/34', '/35', '/36', '/37', '/38', '/39', '/40',
 '/41', '/42', '/43', '/44', '/45', '/46', '/47', '/48', '/49', '/50', '/51',
 '/52', '/53', '/54', '/55', '/56', '/57', '/58', '/59', '/60', '/61', '/62',
 '/63', '/64', '/65', '/66', '/67', '/68', '/69', '/70', '/71', '/72', '/73',
 '/74', '/75', '/76', '/77', '/78', '/79', '/80', '/81', '/82', '/83', '/84',
 '/85', '/86', '/87', '/88', '/89', '/90', '/91', '/92', '/93', '/94', '/95',
 '/96', '/97', '/98', '/99']
for row in reader:
    for field in row:
        for i in st:
            if i in field:
                if i == "/00":
                    a = a + 1
                    #print a
                    if a >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i =="/01":
                    b = b + 1
                    #print b
                    if b >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i =="/02":
                    c = c + 1
                    #print c
                    if c >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i =="/03":
                    d = d + 1
                    #print d
                    if d >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/04":
                    e = e + 1
                    #print e
                    if e >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/05":
                    f = f + 1
                    #print f
                    if f >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/06":
                    g = g + 1
                    #print g
                    if g >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/07":
                    h = h + 1
                    #print h
                    if h >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/08":
                    j = j + 1
                    #print j
                    if j >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/09":
                    k = k + 1
                    #print k
                    if k >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/10":
                    l = l + 1
                    #print l
                    if l >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/11":
                    m = m + 1
                    #print m
                    if m >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/12":
                    n = n + 1
                    #print n
                    if n >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                if i == "/13":
                    o = o + 1
                    #print o
                    if o >12:
                        new = "/20"+i[1:3]
                        fullyear.append(new)
                        break
                new = "/19"+i[1:3]
                fullyear.append(new)
print fullyear

myfile = open('fullyear.csv', 'wb')
wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
wr.writerow(fullyear)
