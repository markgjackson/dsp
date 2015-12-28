from datetime import date
month_numbers = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
                 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

date_start1 = '01-02-2013'    
date_stop1 = '07-28-2015'

date_start2 = '12312013'  
date_stop2 = '05282015'

date_start3 = '15-Jan-1994'
date_stop3 = '14-Jul-2015'

#d0  = date(1994, 1, 15)
#d1  = date(2015, 7, 14)
d1 = date(int(date_start1[6:]),int(date_start1[0:2]),int(date_start1[3:5]))
print d1
d2 = date(int(date_stop1[6:]),int(date_stop1[0:2]),int(date_stop1[3:5]))
print d2
d3 = date(int(date_start2[4:]),int(date_start2[0:2]),int(date_start2[2:4]))
print d3
d4 = date(int(date_stop2[4:]),int(date_stop2[0:2]),int(date_stop2[2:4]))
print d4
d5 = date(int(date_start3[7:]),int(month_numbers[date_start3[3:6]]),int(date_start3[0:2]))
print d5
d6 = date(int(date_stop3[7:]),int(month_numbers[date_stop3[3:6]]),int(date_stop3[0:2]))
print d6


deltaA = d2-d1
deltaB = d4-d3
deltaC = d6-d5

print "The number of days between " + str(d2) + " and " + str(d1) + " is " + str(deltaA.days)
print "The number of days between " + str(d4) + " and " + str(d3) + " is " + str(deltaB.days)
print "The number of days between " + str(d6) + " and " + str(d5) + " is " + str(deltaC.days)
