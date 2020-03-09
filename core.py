from random import randint
class core:
  def __init__(self):
    #self.x=['2020-03-01-14h20','2020-03-02-16h20','2020-03-11-09h20','2020-03-11-17h20']
    #self.y=y=[73,23,12,17]
    self.df={}
    for j in range(1,10):
      user="user%d"%(j)
      self.df[user]={"delivery":[],"duration":{"total":[],"compile":[],"other":[]}}
      for i in range(1,randint(1,50)):
        self.df[user]["delivery"].append("Delivery %d"%(i))
        self.df[user]["duration"]["total"].append(randint(3,120))
        self.df[user]["duration"]["compile"].append(self.df[user]["duration"]["total"][-1]*randint(0,50)/100.)
        self.df[user]["duration"]["other"].append(self.df[user]["duration"]["total"][-1]-self.df[user]["duration"]["compile"][-1])

