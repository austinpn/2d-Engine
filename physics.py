from exceptions import NotInstantiatableException
from assorted import vector_addition, vector_array_summed
from enum import Enum, auto
from collections.abc import Iterator
from numbers import Number
import numpy

__constant_forces = ()
def set_constant_forces(constant_forces):
    if not constant_forces is tuple:
        raise TypeError
    __constant_forces = constant_forces
def get_constant_forces():
    return __constant_forces

class Vector():
    def __init__(self, *vals):
        self._vector = list(vals)
        
    def __setitem__(self, i, val):
        self._vector[i] = val

    def __getitem__(self, i):
        return self._vector[i]
    
    def __len__(self):
        return self.dimension

    def __iter__(self):
        return iter(self._vector)

    def copy(self):
        return Vector(*self._vector.copy())

    @property
    def dimension(self):
        return len(self._vector)
    

    @staticmethod
    def sum(*vectors: Iterator , **kwargs) -> 'Vector':
        if(len)
        targ = vectors[0].copy()
        if('targ_vector' in kwargs):
            targ = kwargs['targ_vector']
        else:
            targ = [0,0]
        
        for i in range(len(targ)):
            for vector in vectors:
                if(len(vector) <= i):
                    continue
                targ[i]+=vector[i]
        return Vector(*targ)

    def __add__(self, term):
        return Vector.sum(self,term)
    def __radd__(self, term):
        return self+term
    
    def add(self, term):
        return Vector.sum(term, targ_vector = self)
    
    #TODO inconsistent with static add, perhaps change to static to be similar
    def multiply(self, factor):
        if(isinstance(factor, Number)):
            for i in range(self.dimension): self._vector[i]*=factor
        else:
            raise 
    
    def __mul__(self, factor):
        clone = self.copy()
        clone.multiply(factor)
        return clone
    
    def __rmul__(self, factor):
        return self*factor
    
    def update(self, vector):
        self.multiply(0)
        self.add(vector)
    
            


class Velocity(Vector):
    def __init__(self, *vals):
        super().__init__(*vals)
        self.__num_nonzero = 0
        #initial zero check
        for val in self._vector:
            if(val!=0):
                self.__num_nonzero+=1

    def __setitem__(self, i, val):
        was_zero = self._vector[i]==0
        self._vector[i] = val
        if(was_zero and self._vector[i]!=0):
            self.__num_nonzero+=1
        elif( (not was_zero) and self._vector[i]==0):
            self.__num_nonzero-=1
    
    @property
    def is_mobile(self):
        return self.__num_nonzero!=0
    
    def copy(self):
        return Velocity(*self._vector.copy())

class PhysicsObject():
    def __init__(self, location , mass , velocity = None):
        if velocity == None:
            velocity = Velocity(0,0)

        self.active_forces = [Vector(0,0)]
        self.velocity = velocity
        self.location = location
        self.mass = mass
    
    def exert_force(self , force):
        vector_addition(self.active_forces[0] , force)
    
    # def move(self):
    #     vector_array_summed(get_constant_forces() , targ_vector=self.velocity , divisor = self.mass)
    #     vector_array_summed(self.active_forces , targ_vector = self.velocity)
    #     vector_addition(self.location , self.velocity)

    def move(self):
        Vector.sum(*get_constant_forces() , targ_vector=self.velocity , divisor = self.mass)
        Vector.sum(*self.active_forces , targ_vector = self.velocity)
        Vector.sum(self.velocity , targ_vector = self.location)

    @staticmethod
    def collision(obj_a: 'PhysicsObject', obj_b: 'PhysicsObject') -> None:
        pass

class WallType(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()

        
