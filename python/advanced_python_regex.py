import csv

f = open('faculty.csv')
csv_f = csv.reader(f)

emailList=[]
uniqueDomains=[]


for row in csv_f:
  for item in row:
 #    print item
    if item.find('@') != -1:
      emailList.append(item)
      domain=item[item.index('@')+1:]
 #     print "The email is: " + item
 #     print "The domain is: " + domain
      
      if not (domain in uniqueDomains):
        uniqueDomains.append(domain)
 #       print "Just added it"

print "Here is the email list:"
print emailList
print "Here is the domain list, containing " + str(len(uniqueDomains)) + " entries"
print uniqueDomains




f = open('emails.csv', 'wb')
writer = csv.writer(f)

for email in emailList:
#  print email
  writer.writerow([email])
f.close()
    

print "Done writing!"
