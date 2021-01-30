import pygame
from objects import GameObjectCollection, CircleObject
from physics import Vector

class Graphics():
    def __init__(self , width , height , background):
        self.width = width
        self.height = height
        self.background = background
        self.game_objects = GameObjectCollection()
        

    def initialize(self):

        pygame.init()
        self.screen = pygame.display.set_mode((self.width , self.height))
        self.screen.fill(self.background)
        
        self.player_object = CircleObject(self.screen , Vector(self.width // 2 , self.height // 2) , 15 )
        self.player_force = [0,0]
        self.player_object.physics.active_forces.append(self.player_force)
        self.game_objects.add_object(self.player_object)

        self.passive_object = CircleObject(self.screen , [(self.width // 2) + 100 , (self.height // 2) - 200] , 30 , mass=2)
        self.game_objects.add_object(self.passive_object)
        

        self.redraw_game()
        
    def redraw_game(self):
        self.screen.fill(self.background)
        self.game_objects.redraw_all()
        pygame.display.update()
        
    def quit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                self.player_force[1] += -1
            if event.type == pygame.KEYUP and event.key == pygame.K_w:
                self.player_force[1] -= -1
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                self.player_force[1] += 1
            if event.type == pygame.KEYUP and event.key == pygame.K_s:
                self.player_force[1] -= 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.player_force[0] += 1
            if event.type == pygame.KEYUP and event.key == pygame.K_d:
                self.player_force[0] -= 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                self.player_force[0] += -1
            if event.type == pygame.KEYUP and event.key == pygame.K_a:
                self.player_force[0] -= -1


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
        

