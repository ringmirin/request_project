import json, requests
# def request1():
x=requests.get('http://saral.navgurukul.org/api/courses')
file1=x.json()
print("Sl.  COURSE---- ID")
with open("api1.json","w")as fh:
   json.dump(file1,fh,indent=4)
id=[]
for i in file1:
   a=1
   for j in file1[i]:
      print(a,"-",j["name"],j["id"])
      id.append(j["id"])
      a+=1
# request1()
def request2():
   global user2,slug
   user1=int(input("select chapter no: "))-1
   y=requests.get('http://saral.navgurukul.org/api/courses/'+id[user1]+'/exercises')
   file2=y.json()
   print("-----EXERCISES-----")
   # print(file2)
   with open("api2.json","w") as fh:
      json.dump(file2,fh,indent=4)
   slug=[]
   for i in file2:
      b=1
      for k in file2[i]:
         print(b,k["name"])
         slug.append(k["slug"])
         b+=1
request2()

user2=int(input("choose the slug no. : "))
def request():
   url3=requests.get('http://saral.navgurukul.org/api/courses/'+str(user2)+'/exercise/getBySlug?slug='+str(slug[user2]))
   api2=url3.json()
   with open("api3.json","w")as f:
      json.dump(api2,f,indent=5)
   print(api2)
# request2()
request()
for index in range(len(slug)):
   user=input("enter n/p: ")
   if user=="n":
      user2=user2+1
      if user<str(len(slug)):
         request()
      else:
         print("content does not exist ")
         # break
   elif user=="p":
      user2=user2-1
      if user>=str(len(slug)):
         request()
      else:
         print("content does not exist")
         break
   else:
      print("exit")



      


   
      
      

