from enum import Enum, auto
from collections.abc import Sequence
from numbers import Number

import physics.vector as vector
from physics.vector import Vector


class PhysicsObject():
    __global_forces = vector.get_inert_vector(2)
    def __init__(self, location , mass , velocity = None):
        if velocity == None: self.velocity = Vector(0,0)
        else: self.velocity = velocity
        self.applied_force = Vector(0,0)
        self._location = location
        self._mass = mass
        self._object_type = ObjectType.DEFAULT

    def exert_force(self , force: Sequence):
        self.applied_force+=force
    def move(self):
        self.velocity.update( Vector.sum(self.applied_force,self.__global_forces, self.velocity))
        self._location.update(self._location+self.velocity)

    
    @staticmethod
    def get_global_force()->Vector:
        return PhysicsObject.__global_forces.copy()
    @staticmethod
    def set_global_force(value: Sequence):
        if(not isinstance(value, Sequence) and len(value)!=2): raise ValueError
        PhysicsObject.__global_forces = Vector(*value)

    @staticmethod
    def check_collision(obj_a:'PhysicsObject', obj_b: 'PhysicsObject')->bool:
        x_distance = obj_a._location[0] - obj_b._location[0]
        y_distance = obj_a._location[0] - obj_b._location[0]

        if(obj_a._object_type==ObjectType.CIRCLE and obj_b._object_type==ObjectType.CIRCLE):
            radii_sum = obj_a._radius + obj_b._radius
            return radii_sum**2 < (x_distance**2) + (y_distance**2)
        
        if(
            obj_a._object_type == ObjectType.WALL   and obj_b._object_type == ObjectType.CIRCLE or
            obj_a._object_type == ObjectType.CIRCLE and obj_b._object_type == ObjectType.WALL):
            if(obj_a._object_type== ObjectType.WALL): wall = obj_a
            else: wall = obj_b

            if(wall.wall_type == WallType.LEFT or wall.wall_type == WallType.RIGHT):
                return x_distance**2<=0
            else:
                return y_distance**2<=0

        return False
    
class CirclePhysicsObject(PhysicsObject):
    def __init__(self, location , mass , radius, velocity = None):
        super().__init__(location, mass, velocity)
        self._object_type = ObjectType.CIRCLE
        self._radius = radius

class Wall(PhysicsObject):
    def __init__(self, wall_type, relevant_coord):
        if(wall_type == WallType.LEFT or wall_type == WallType.RIGHT):
            super().__init__(Vector(relevant_coord, 0), None)
        else:
            super().__init__(Vector(0, relevant_coord), None)
        self._object_type = ObjectType.WALL
        self.__wall_type = wall_type
    @property
    def wall_type(self):
        return self.__wall_type

class WallType(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()

class ObjectType(Enum):
    DEFAULT = auto()
    CIRCLE = auto()
    WALL = auto()

        
