import pygame
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()

class Rectangle():
    def __init__(self,color,dimentions,width,radius):
        self.color = color
        self.dimentions = dimentions
        self.width = width
        self.radius = radius
    def display(self):
        pygame.draw.rect(screen,self.color,self.dimentions,self.width,self.radius)

pinkrect = Rectangle("pink",(125,10,450,450),60,4)
pinkrect.display()
bluerect = Rectangle("blue",(175,200,350,367),22,0)
bluerect.display()
yellowrect = Rectangle("yellow",(40,300,190,70),5,10)
yellowrect.display()
redrect = Rectangle("red",(470,300,190,70),5,10)
redrect.display()
greenrect = Rectangle("green",(300,300,190,400),5,10)
greenrect.display()

pygame.display.update()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:  
            exit()