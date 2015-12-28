import csv

f = open('football.csv')
csv_f = csv.reader(f)
team=[]
goals=[]
goalsAllowed=[]

for row in csv_f:
 # print row
  if row[0] != "Team":
      team.append(row[0])
      goals.append(int(row[5]))
      goalsAllowed.append(int(row[6]))

print team
print goals
print goalsAllowed

diffList=[]
for i in range(0,len(goals)):
    diffList.append(goals[i]-goalsAllowed[i])

print diffList

minDiff=abs(diffList[0])
minTeam=""

for i in range(0,len(goals)):
    if abs(diffList[i]) < minDiff:
        minDiff = abs(diffList[i])
        minTeam=team[i]

print minTeam
