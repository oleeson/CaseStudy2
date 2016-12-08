import pandas as pd
import csv
import re

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
        return start

tempinusa = pd.read_csv('usa.csv')
tempinusa= tempinusa[tempinusa.Date.str.len() <= 8]
save_Date = tempinusa.Date

thenewdates = open('fullyear.csv', 'rb')
reading = csv.reader(thenewdates)

newdatelist = []
for row in reading:
    for i in row:
        newdatelist.append(i)
#print newdatelist

olddatelist = []
for olddate in save_Date:
    olddatelist.append(olddate)
#print olddatelist

neededlist =[]
count=0
if count <= len(olddatelist):
    for field in olddatelist:
        #print "field", field
        loc = find_nth(field, '/', 2)
        #print "loc" , loc
        old =  field[loc:]
        #print "old", old
        splitfield = list(field)
        #print "splitfield[loc:]", splitfield[loc:]
        newfield = list(newdatelist[count])
        #print "newfield" , newfield
        splitfield[loc:] = newfield
        #print "splitfield" , splitfield[loc:]
        field = "".join(splitfield)
        #print "field", field
        #print "--------\n"
        neededlist.append(field)
        count = count + 1
#print neededlist

properdates = pd.Series(neededlist)
#print properdates

tempinusa["newdates"] = properdates.values
#print temp.newdates
print tempinusa.head()
print tempinusa.tail()


tempinusa.to_csv('usaclean.csv')
