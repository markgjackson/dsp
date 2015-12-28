import csv
from pprint import pprint
from operator import itemgetter, attrgetter, methodcaller

f = open('faculty.csv')
csv_f = csv.reader(f)

emailList=[]
uniqueDomains=[]
dict={}
newDict={}


for row in csv_f:
  fullName = row[0]
  #print fullName
  done=False
  for i in range(0, len(fullName)-1):
    #print "The value of i is "  + str(i)
    #print fullName[i:]
    if (fullName[i:].find(" ") == -1) and done==False:
      #print "I'm about to figure out the last name"
      lastName = fullName[i:]
      firstName = fullName[:i-1]
      spaceLoc = firstName.find(" ")
      if spaceLoc != -1:
        firstName = firstName[:spaceLoc]      
      done = True
      #print "The last name is " + lastName
  #print "All done with figuring out last name"

  longTitle = row[2]
  #print "Long title: "+ longTitle
  if longTitle != " title":
    title = longTitle[:longTitle.index("Professor")+9]
    #print "just shortened the title"
  else:
    title = " title"

  degrees = row[1]
  entry = [degrees[1:],title,row[3]]
  if dict.has_key(lastName):
    #print lastName + " is already there, adding one more"
    existingEntry=dict[lastName]
    #print "The existing one is " + str(existingEntry)
    #print "I'm going to add " + str(entry)
    existingEntry.append(entry)
    #print "The new one will be " + str(existingEntry)
    dict[lastName] = existingEntry
  else:
    #print "Creating a new entry for " + lastName + " of " + str(entry)
    dict[lastName] = [entry]



  thisKey=(firstName,lastName)
  #print "Now processing " + firstName + " " + lastName
  if lastName != "name":
    newDict[thisKey]=entry

sortedDict={}
sortedKeys=sorted(newDict,key = itemgetter(1))
for key in sortedKeys:
    sortedDict[key] = newDict[key]
    print str(key) + "," + str(sortedDict[key])
  
  #print "Just updated "+ str(dict[lastName])  

  
f.close()

print "\n \n"    
print "Old dictionary: "
pprint(dict)
print "\n \n"
print "New  dictionary: "
pprint(newDict)


