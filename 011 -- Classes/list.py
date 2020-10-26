class person:
    def __init__ (self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
        
    def greet(self):
        return "Hello. My name is " + self.name + ". I am a " + self.job + ". My age is " + self.age + "."

people = [person("AG", "student", "6"),person("EE", "toddler", "3")]

people.append(person("Blaize", "Programmer", "40"))

for persons in people:
    print(persons.greet())
