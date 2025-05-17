import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
purple = (100,0,255)
pygame.display.update()

class square:
    def __init__(self,color,pos,side,width):
        self.c_color = color
        self.pos = pos
        self.side = side
        self.width = width
        self.square_surface = screen
    
    def draw(self):
        Draw_Square = pygame.draw.rect(self.square_surface, self.c_color,(self.pos[0],self.pos[1], self.side, self.width))
        return Draw_Square

    def grow(self,s):
        self.side = self.side + s
        self.width = self.width + s
        Draw_Square = pygame.draw.rect(self.square_surface, self.c_color,(self.pos[0],self.pos[1], self.side, self.width))
        return Draw_Square

obj = square(purple,(250,250),100,100)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill((255,255,255))
            obj.draw()
            pygame.display.update()
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill((255,255,255))
            obj.grow(25)
            pygame.display.update()
