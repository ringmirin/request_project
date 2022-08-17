import json
import requests
x=requests.get('http://saral.navgurukul.org/api/courses')
file1=x.json()
print("Sl.  COURSE---- ID")
with open("r1.json","w")as fh:
   json.dump(file1,fh,indent=4)
id=[]
for i in file1:
   a=1
   for j in file1[i]:
      print(a,"-",j["name"],j["id"])
      id.append(j["id"])
      a+=1
global user1
user1=int(input("select chapter no: "))-1
y=requests.get('http://saral.navgurukul.org/api/courses/'+id[user1]+'/exercises')
file2=y.json()
with open("r2.json","w") as fh:
   json.dump(file2,fh,indent=4)
slug=[]
for i in file2:
   b=1
   
   for k in file2[i]:
      print(b,k["name"])
      slug.append(k["slug"])
      b+=1
user3=int(input("select the course: "))
z=requests.get('http://saral.navgurukul.org/api/courses/'+str(user1)+'/exercise/getBySlug?slug='+str(slug[user3]))
file3=z.json()
with open("r3.json","w") as fh:
   json.dump(file3,fh,indent=4)
print(file3)














