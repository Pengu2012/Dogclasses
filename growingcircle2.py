import pygame
pygame.init()
WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.update()
screen.fill("white")

class GrowingCircle():
    def __init__ (self,rgb,pos,rad,wid):
        self.rgb = rgb
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.surface = screen
    def draw(self):
        pygame.draw.circle(self.surface,self.rgb,self.pos,self.rad, self.wid)
    def grow(self,r):
        self.rad = self.rad + r
        pygame.draw.circle(self.surface,self.rgb,self.pos,self.rad, self.wid)


bluecircle = GrowingCircle((0,0,255),(350,350),10,50)



pygame.display.update()
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:  
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            bluecircle.draw()
            pygame.display.update()
        if i.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            bluecircle.grow(10)
            pygame.display.update()
        if i.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            blackcircle = GrowingCircle((0,0,0),(pos),10,5)
            blackcircle.draw()
            pygame.display.update()