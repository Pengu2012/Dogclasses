import pygame
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()
screen.fill("white")

class Circle():
    def __init__(self,rgb,pos,radius,thickness):
        self.rgb = rgb
        self.pos = pos
        self.radius = radius
        self.thickness = thickness
    def display(self):
        pygame.draw.circle(screen,self.rgb,self.pos,self.radius,self.thickness)

redcircle = Circle((255,0,0),(545,250),70,7)
redcircle.display()
greencircle = Circle((0,255,0),(475,315),70,7)
greencircle.display()
bluecircle = Circle((0,0,255),(250,250),70,7)
bluecircle.display()
yellowcircle = Circle((255,255,0),(315,315),70,7)
yellowcircle.display()
blackcircle = Circle((0,0,0),(395,250),70,7)
blackcircle.display()


pygame.display.update()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:  
            exit()