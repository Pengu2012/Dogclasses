class Dog():
    legs = 4
    ears = 2
    tails = 1
    eyes = 2
    can_run = True
    can_swim =True
    can_eat_chocolate = False

    def eat(self):
        print('Nom nom')
    def bark(self):
        print('Woof Arf')
    def mad(self):
        print('grrrrrr')
    
Husky = Dog()
Golden_retriver = Dog()
Dalmation = Dog()
Shiba_inu = Dog() 
bulldog = Dog()
German_bloodhound = Dog()


print(bulldog.eyes)
Husky.eat()
print(Dalmation.can_run, Dalmation.can_eat_chocolate)
Golden_retriver.mad()
Shiba_inu.bark()
print(German_bloodhound.can_swim)