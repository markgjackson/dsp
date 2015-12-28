# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
if count > 9:
 countString = "many"
else:
    countString = str(count)

print "Number of donuts: " + countString





def both_ends(s):
firstPart = s[0:2]
secondPart = s[-2:-1]

print firstPart + secondPart + s[len(s)-1]



def fix_start(s):
editedS = s[1:]

print s[0] + editedS.replace(s[0],"*")



def mix_up(s1, s2):
s1New = s2[0:2]+s1[2:]
s2New = s1[0:2]+s2[2:]

print s1New + " " + s2New




def verbing(s):
if len(s) > 2:
    if s[-3:] == "ing":
        print s + "ly"
    else:
        print s + "ing"
else:
    print s
    
        



def not_bad(s):
notLoc=s.find("not")

if notLoc != -1:
    s2 = s[notLoc+3:]
    badLoc = s2.find("bad")
    if badLoc != -1:
        print s[:notLoc] + "good" + s2[badLoc+3:]
    else:
        print s

else:
    print s
    
        



def front_back(s1, s2):

if len(s1) % 2 == 0:
    s1Front = s1[:len(s1)/2]
    s1Back = s1[len(s1)/2:]
else:
    s1Front=s1[:(len(s1)+1)/2]
    s1Back = s1[(len(s1)+1)/2:]

if len(s2) % 2 == 0:
    s2Front = s2[:len(s2)/2]
    s2Back = s2[len(s2)/2:]
else:
    s2Front=s2[:(len(s2)+1)/2]
    s2Back = s2[(len(s2)+1)/2:]

print s1Front + s2Front + s1Back + s2Back

