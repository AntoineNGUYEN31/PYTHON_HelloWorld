import requests
import json

class core:
  def __init__(self):
    #init database
    self.update()

  def update(self):
    self.df={}
    #get data from back end
    reponse=requests.get('http://localhost:8080/database/').json()

    #build up dataframe for Dash plotting
    for block in reponse["userList"]:
      # dict keys are expected: "label", "epoch", ...
      user=block["userLogin"]
      print(user)
      self.df[user]={"delivery":[],"duration":{}}
      #print(block["userData"])
      #print(type(block["userData"]))
      details=None
      for case in json.loads(block["userData"].replace("'",'"')):
        if details==None:
          details=list(case.keys())
          #print(details)
          details.remove("label")
          details.remove("epoch")
          for item in details:
            self.df[user]["duration"][item]=[]
        self.df[user]["delivery"].append(case["label"]+"-"+str(case["epoch"]))
        for item in details:
          self.df[user]["duration"][item].append(case[item])
    #trick to no bug Dash, dataframe should not be emty
    if self.df=={}:
      self.df={"testUser":{"delivery":["Test"],"duration":{"Total":[10]}}}
