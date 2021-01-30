import pygame
import physics as physlib
import numpy
from exceptions import InvalidOperationException, NotInstantiatableException
class GameObjectCollection():
    def __init__(self):
        self.active_objects = []
    def add_object(self, newObj):
        if(newObj in self.active_objects or issubclass(GameObject , type(newObj))):
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
        self.parent_surface = parent_surface
        self.location = location
        self.last_location = location.copy()
        self.physics = None
        
    
            

    def draw_image(self):
        pass
    


class CircleObject(GameObject):
    def __init__(self, parent_surface , location , radius , mass = 1, color = 0):
        super().__init__(parent_surface, location)
        
        self.radius = radius
        self.color = color
        self.physics = physlib.PhysicsObject(self.location , mass)
    
    def draw_image(self):
        self.physics.move()
        pygame.draw.circle(self.parent_surface , self.color , self.location , self.radius)

class WallObject(GameObject):
    def __init__(self, location):
        super().__init__(None, location)

def collision_check(obj_a: GameObject, obj_b: GameObject) -> bool:
    #pythagorean distance
    distance = numpy.sqrt( (obj_a.location[0] - obj_b.location[0])**2 + (obj_a.location[1] - obj_b.location[1])**2 )
    if(type(obj_a) == CircleObject and type(obj_b) == CircleObject):
        return (distance - (obj_a.radius + obj_b.radius)) <= 0
    if(type(obj_a) == CircleObject and type(obj_b) == WallObject):
        return (distance - obj_a.radius) <=0
    if(type(obj_b) == CircleObject and type(obj_a) == WallObject):
        return (distance - obj_b.radius) <=0
    
    