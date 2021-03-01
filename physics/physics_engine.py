import time, threading, multiprocessing

from .physics_objects import PhysicsObject

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