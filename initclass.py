class Family():
    def __init__(self,name,age,height,job,sleep):
        self.name = name
        self.age = age
        self.height = height
        self.job = job
        self.sleep = sleep
    
    def trip(self):
        print("Lets go on a road trip!")

Mother = Family("Mary",42,"178 cm","Banker","8 hours")
Father = Family("John",43,"189 cm","Chef","7 hours")
Son = Family("Mark", 15, "168 cm","None","9 hours")
Daughter  = Family("Emily", 12, "154 cm", "None", "10 hours")
Son2 = Family("Ken",7,"140 cm", "None", "12 hours")

print(Mother.job)
print(Father.height)
print(Son.name)
print(Daughter.sleep)
Son2.trip()