import pygame
from exceptions import InvalidOperationException

class GameObjectCollection():
    def __init__(self):
        self.active_objects = []
    def add_object(self, newObj):
        if(newObj in self.activeObjects or type(newObj)!=GameObject):
            raise InvalidOperationException

        self.active_objects.append(newObj)
    def remove_object(self, oldObj):
        if(not (oldObj in self.activeObjects) or type(oldObj)!=GameObject):
            raise InvalidOperationException
        self.active_objects.remove(oldObj)
    def redraw_all(self):
        for obj in self.active_objects:
            obj.draw_image()

class GameObject():
    def __init__(self, parent_surface, location):
        self.state_change = False
        self.parent_surface = None
        self.location = location
        self.last_location = location.copy()

    def render(self):
        pass



class CircleObject(GameObject):
    def __init__(self, parent_surface , location , radius , color = 0):
        super().__init__(parent_surface, location)
        
        self.radius = radius
        self.color = color
    def draw_image(self):
        pygame.draw.circle(self.parent_surface , self.color , self.radius)

    


        
    