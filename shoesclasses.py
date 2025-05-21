class Shoes():
    def __init__(self,price,age,handyness,style): # 1 is bad 10 is best
        self.price =  price
        self.age = age
        self.handyness = handyness
        self.style = style
    
    def pain(self):
        print("OWW")

shoe = Shoes(30,"2years",9,7)
heels =Shoes(80,"4years",3,9)
slippers = Shoes(10,"1years",6,4)
boots  = Shoes(60,"4years",8,10)

print(shoe.price)
print(heels.age)
print(slippers.handyness)
print(boots.style)
heels.pain()