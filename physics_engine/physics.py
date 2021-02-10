import physics_engine.vector as vector
from physics_engine.vector import Vector
from enum import Enum, auto
from collections.abc import Sequence
from numbers import Number

class PhysicsObject():
    __global_forces = vector.get_inert_vector(2)
    def __init__(self, location , mass , velocity = None):
        if velocity == None: self._velocity = Vector(0,0)
        else: self._velocity = velocity
        self._applied_force = Vector(0,0)
        self._location = location
        self._mass = mass
    
    @staticmethod
    def get_global_force()->Vector:
        return PhysicsObject.__global_forces.copy()
    @staticmethod
    def set_global_force(value: Sequence):
        if(not isinstance(value, Sequence) and len(value)!=2): raise ValueError
        PhysicsObject.__global_forces = Vector(*value)

    #TODO write exert_force()
    def exert_force(self , force: Sequence):
        raise NotImplemented()
    
    #TODO write move
    def move(self):
        raise NotImplemented

    
class Engine():
    raise NotImplemented

class WallType(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()

        
