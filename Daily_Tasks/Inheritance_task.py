# Inheritance Task
class animal:
    def __init__(self,type,breed) -> None:
        self.type=type
        self.breed=breed
    def animal_name(self):
        print(self.type,self.breed)
class cat(animal):
    pass
y=cat("A","Persian")
y.animal_name()

