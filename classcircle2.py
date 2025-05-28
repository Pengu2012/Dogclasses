import pygame
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()
screen.fill("white")

class Circle():
    def __init__(self,rgb,pos,radius):
        self.rgb = rgb
        self.pos = pos
        self.radius = radius
    def display(self):
        pygame.draw.circle(screen,self.rgb,self.pos,self.radius)

redcircle = Circle((255,0,45),(545,250),70)
redcircle.display()
greencircle = Circle((0,55,5),(475,315),70)
greencircle.display()
bluecircle = Circle((245,205,100),(250,250),70)
bluecircle.display()
yellowcircle = Circle((255,255,45),(315,315),70)
yellowcircle.display()
blackcircle = Circle((5,6,7),(395,250),70)
blackcircle.display()


pygame.display.update()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:  
            exit()
