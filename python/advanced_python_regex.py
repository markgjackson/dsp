import csv

f = open('faculty.csv')
csv_f = csv.reader(f)

# DegreeList=["PhD","ScD","MD","JD","BSEd"]
degreeList=[]
frequencyList=[]


for row in csv_f:
#  print row
  cleanedDegrees=row[1].replace(".","")

  wordDegree = ""
  for char in cleanedDegrees:
    if char != " ":
      wordDegree = wordDegree + char
#      print "The character added is '" + char + "'"
    else:
#      print "Met space, the wordDegree is: '" + wordDegree + "'"
      if not (wordDegree in degreeList):
#        print "New degree: '" + wordDegree + "'"
        degreeList.append(wordDegree)
        frequencyList.append(1)
        wordDegree=""
      else:
#        print "Old degree: '" + wordDegree + "'"
        whereIsit = degreeList.index(wordDegree)
        frequencyList[whereIsit]=frequencyList[whereIsit]+1
        wordDegree=""
#  print "End of cleanedDegree, the wordDegree is: '" + wordDegree + "'"
  if not (wordDegree in degreeList):
#    print "New degree: '" + wordDegree + "'"
    degreeList.append(wordDegree)
    frequencyList.append(1)
  else:
#    print "Old degree: '" + wordDegree + "'"
    whereIsit = degreeList.index(wordDegree)
    frequencyList[whereIsit]=frequencyList[whereIsit]+1
#  print "Done with that word, moving on"
  wordDegree=""
#  print "Done with that cleaned degree, moving on"

f.close() 
print "The list of degrees is:"
print degreeList[2:]
print "The corresponding frequency is:"
print frequencyList[2:]

print "\n \n"

f = open('faculty.csv')
csv_f = csv.reader(f)
titleList=[]
frequencyList=[]

for row in csv_f:
  longTitle = row[2]
#  print "Long title: "+ longTitle
  if longTitle != " title":
    title = longTitle[:longTitle.index("Professor")+9]
#    print "Short title: " + title
    if not (title in titleList):
      titleList.append(title)
      frequencyList.append(1)
#      print "New title!"
    else:
      whereIsIt = titleList.index(title)
      frequencyList[whereIsIt] = frequencyList[whereIsIt]+1
#      print "Old title!"
f.close()
print "The list of titles is:"
print titleList
print "The corresponding frequency is:"
print frequencyList

