class person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def greet(self):
        return "My name is " + self.name + ". I am a " + self.job + "."

class coder(person):
    def __init__(self, name, job, language):
        super().__init__(name,job)
        self.language = language

    def greet(self):
        return "My name is " + self.name + ". I am a " + self.job + ". I code in " + self.language + "."
    
blaize = person("Blaize", "Architect")
print(blaize.greet())
