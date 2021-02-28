from enum import Enum, auto
from collections.abc import Sequence
from numbers import Number
import time, threading, multiprocessing

import physics_engine.vector as vector
from physics_engine.vector import Vector


class PhysicsObject():
    __global_forces = vector.get_inert_vector(2)
    def __init__(self, location , mass , velocity = None):
        if velocity == None: self._velocity = Vector(0,0)
        else: self._velocity = velocity
        self._applied_force = Vector(0,0)
        self._location = location
        self._mass = mass
        self._object_type = ObjectType.DEFAULT

    #TODO write exert_force()
    def exert_force(self , force: Sequence):
        self._applied_force+=force
    def move(self):
        self._velocity.update( Vector.sum(self._applied_force,self.__global_forces, self._velocity))
        self._location.update(self._location+self._velocity)

    
    @staticmethod
    def get_global_force()->Vector:
        return PhysicsObject.__global_forces.copy()
    @staticmethod
    def set_global_force(value: Sequence):
        if(not isinstance(value, Sequence) and len(value)!=2): raise ValueError
        PhysicsObject.__global_forces = Vector(*value)

    @staticmethod
    def check_collision(obj_a:'PhysicsObject', obj_b: 'PhysicsObject')->bool:
        if(obj_a._object_type==ObjectType.CIRCLE and obj_b._object_type==ObjectType.CIRCLE):
            x_distance = obj_a._location[0] - obj_b._location[0]
            y_distance = obj_a._location[0] - obj_b._location[0]
            radii_sum = obj_a._radius + obj_b._radius
            return radii_sum**2 < (x_distance**2) + (y_distance**2)
    

    
class CirclePhysicsObject(PhysicsObject):
    def __init__(self, location , mass , radius, velocity = None):
        super().__init__(location, mass, velocity)
        self._object_type = ObjectType.CIRCLE
        self._radius = radius
    
class Engine():
    def __init__(self):
        self.__loaded_objects = []
        self.__active_engine = False
        self.__lock = None
    def register_object(self, obj:PhysicsObject):
        self.__loaded_objects.append(obj)
    def remove_object(self, obj:PhysicsObject):
        self.__loaded_objects.remove(obj)
    def __update_physics(self):
        print("Entering physics loop")
        while self.__active_engine:
            
            self.__lock.acquire()
            for obj in self.__loaded_objects:
                obj.move()
            time.sleep(.03)
            self.__lock.release()
        
        self.__lock = None
        print("Closing physics thread")
    def kill(self):
        self.__active_engine = False
    
    def run(self, lock):
        self.__active_engine = True
        self.__lock = lock
        
        update_thread = threading.Thread(target=self.__update_physics, name="physics thread", daemon=True)
        update_thread.start()

    def run_process(self, lock):
        self.__active_engine = True
        self.__lock = lock
        
        update_process = multiprocessing.Process(target=self.__update_physics, name="physics thread", daemon=True)
        update_process.start()


class WallType(Enum):
    LEFT = auto()
    RIGHT = auto()
    TOP = auto()
    BOTTOM = auto()

class ObjectType(Enum):
    DEFAULT = auto()
    CIRCLE = auto()

        
