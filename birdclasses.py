class Bird():
    eyes = 2
    feet = 2
    wings = 2
    can_lay_eggs = True
    can_fly = True
    def speak(self):
       print("chirp chirp")
    def fly(self):
      print("flap flap")

pigeon = Bird()
crow = Bird()
raven = Bird()
robin = Bird()
woodpecker = Bird()

print(pigeon.can_fly)
crow.fly()
print(raven.eyes, raven.wings)
raven.speak()
print(woodpecker.can_lay_eggs)
print(robin.feet)