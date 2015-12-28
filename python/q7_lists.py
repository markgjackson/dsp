# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
sCount = 0

for words in sList:
    if len(words) > 1:
        if words[0]==words[len(words)-1]:
            sCount = sCount + 1

print sCount



def front_x(words):
xList = []
otherList = []

for words in sList:
    if words[0]=="x":
        xList.append(words)
    else:
        otherList.append(words)

print sorted(xList) + sorted(otherList)



def sort_last(tupList):
sortedList=[]
count=0

while count<10:
    for t in tupList:
        if t[len(t)-1] == count:
            sortedList.append(t)
    count=count+1

print sortedList



def remove_adjacent(nList):
newList = []
nPrev = 10

for n in nList:
    if n != nPrev:
        newList.append(n)
        nPrev=n

print newList



def linear_merge(s1, s2):
sCombined = []
count1 = 0
count2 = 0

while (count1 < len(s1)) and (count2 < len(s2)):
    if s1[count1] < s2[count2]:
        sCombined.append(s1[count1])
        count1 = count1+1
    else:
        sCombined.append(s2[count2])
        count2 = count2+1

print sCombined + s1[count1:] + s2[count2:]

