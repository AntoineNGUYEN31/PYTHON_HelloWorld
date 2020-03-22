from random import randint
from time import time
import requests

masterMarker=["Exploitation","Integration","Validation"]
detailMarker=["Compilation","Copy","Backup","CVStag"]
myURL='http://localhost:8080/database/'

def httpPOST(myURL,myLOGIN,myDATA):
  data={"userLogin":myLOGIN,"userData":str(myDATA)}
  response = requests.post(myURL, json=data)
  #print(response.status_code)


if __name__=="__main__":
  for j in range(1,6):
    myLOGIN="user%d"%(j)
    myDATA=[]
    for i in range(1,randint(5,20)):
      temp={}
      temp["label"]=masterMarker[randint(0,len(masterMarker)-1)]
      temp["epoch"]=int(time())+i
      temp["Total"]=randint(3,120)
      rest=temp["Total"]
      for e in detailMarker:
        temp[e]=rest*randint(0,100)/100.
        rest=rest-temp[e]
      temp["Other"]=rest
      myDATA.append(temp)
    #POST data
    httpPOST(myURL,myLOGIN,myDATA)
  


"""

mystr='[{"label":"Exploitation","epoch":1584821319,"Total":24.4,"Compile":10.1,"Copy":5.2,"Backup":1},{"label":"Integration","epoch":1584841319,"Total":34.4,"Compile":20.1,"Copy":5.2,"Backup":1}]'
data = {"userLogin":"ng7f949","userData":mystr}
response = requests.post('http://localhost:8080/database/', json=data)



    #self.x=['2020-03-01-14h20','2020-03-02-16h20','2020-03-11-09h20','2020-03-11-17h20']
    #self.y=y=[73,23,12,17]
    
    for j in range(1,10):
      user="user%d"%(j)
      self.df[user]={"delivery":[],"duration":{"total":[],"compile":[],"other":[]}}
      for i in range(1,randint(1,50)):
        self.df[user]["delivery"].append("Delivery %d"%(i))
        self.df[user]["duration"]["total"].append(randint(3,120))
        self.df[user]["duration"]["compile"].append(self.df[user]["duration"]["total"][-1]*randint(0,50)/100.)
        self.df[user]["duration"]["other"].append(self.df[user]["duration"]["total"][-1]-self.df[user]["duration"]["compile"][-1])
"""