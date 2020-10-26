class person:
    def __init__ (self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
        
    def greet(self):
        return "Hello. My name is " + self.name + ". I am a " + self.job + ". My age is " + self.age + "."
    
ag = person("AG", "student", "6")
print(ag.greet())
ee = person("EE", "toddler", "3")
print(ee.greet())

    