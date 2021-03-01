import time, threading, multiprocessing

import pygame

from .graphics_objects import GraphicsObject
class Renderer():
    def __init__(self, game_size, primary_surface):
        self.__loaded_visuals = []
        self.__game_size = game_size
        self.__primary_surface = primary_surface
        self.__screen = None
        self.__lock = None
        self.__active_rendering = False

    def __update_graphics(self):
        while(self.__active_rendering):
            # self.__primary_surface.surface.fill(self.__primary_surface.transparent_color)
            self.__primary_surface.surface.fill(pygame.Color("#ffffff"))
            
            self.__lock.acquire()
            for obj_list in self.__loaded_visuals:
                for obj in obj_list:
                    obj.render()
            self.__lock.release()

            self.__screen.blit(self.__primary_surface.surface, [0,0])
            pygame.display.update()

            time.sleep(.03)
        self.__lock = None
        print("Closing graphics thread")

    def register_object(self, obj: GraphicsObject, priority):
        if(len(self.__loaded_visuals)<=priority):
            len_dif = priority - len(self.__loaded_visuals) + 1
            self.__loaded_visuals.extend([[]]*len_dif)
        self.__loaded_visuals[priority].append(obj)
    def run(self, lock):
        self.__lock = lock

        pygame.init()
        self.__screen = pygame.display.set_mode(self.__game_size)
        self.__active_rendering = True
        pygame.display.flip()
        
        graphics_thread = threading.Thread(target=self.__update_graphics, name = "rendering thread", daemon=True)
        graphics_thread.start()

    def run_process(self, lock):
        self.__lock = lock

        pygame.init()
        self.__screen = pygame.display.set_mode(self.__game_size)
        self.__active_rendering = True
        pygame.display.flip()
        

        graphics_process = multiprocessing.Process(target=self.__update_graphics, name = "rendering thread", daemon=True)
        graphics_process.start()
        # graphics_thread = threading.Thread(target=self.__update_graphics, name = "rendering thread", daemon=True)
        # graphics_thread.start()
    def kill(self):
        self.__active_rendering = False
        time.sleep(.5)
        pygame.quit()

