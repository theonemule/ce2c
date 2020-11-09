import json

class person:
   def __init__(self, name, job):
      self.name = name
      self.job = job
      
   def greet(self):
      return "My name is " + self.name + ". I am a "+ self.job + "."
      
blaize = person("blaize", "programmer")    
x = json.dumps(blaize.__dict__)

print (x)

blaizeCloneDict = json.loads(x)
blaizeClone = person(**blaizeCloneDict)
print (blaizeClone.greet())



