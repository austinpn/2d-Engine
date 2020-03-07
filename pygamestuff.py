import pygame

class Graphics():
    def __init__(self , width , height , background):
        self.width = width
        self.height = height
        self.background = background

    def initialize(self):

        pygame.init()
        self.screen = pygame.display.set_mode((self.width , self.height))
        self.screen.fill(self.background)
        pygame.display.update()

    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def pyupdate(self):
        pygame.display.update()
    def drawPolygon(self , color , points , width = 0):
        pygame.draw.polygon(self.screen , color , points , width)

    def drawPolygonArr(self , polyarr):
        # print(polyarr)
        self.screen.fill(self.background)
        for i in range(len(polyarr)):
            self.drawPolygon(polyarr[i].color , polyarr[i].shape , polyarr[i].width)
        

