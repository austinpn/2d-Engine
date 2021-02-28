from enum import Enum
import pygame
import time
import threading, multiprocessing




class Renderable():
    def render(self):
        pass

class GraphicsObject(Renderable):
    transparent_color = pygame.Color(74,65,42)
    def __init__(self, parent_obj, location, width, height, load_img=False):
        super().__init__()
        self.location = location
        self.has_img = load_img
        self.parent_surface = parent_obj.surface
        
        self.surface = pygame.Surface([width, height])
        self.surface.set_colorkey(self.transparent_color)


class Circle(GraphicsObject):
    def __init__(self, parent_obj, location, radius, load_img=False):
        super().__init__(parent_obj, location, radius*2, radius*2, load_img)
        self.radius = radius
        pygame.draw.circle(self.surface, pygame.Color("#2931b3"), [self.radius,self.radius], self.radius)
    def render(self):
        self.parent_surface.blit(self.surface, self.location)


class PrimarySurface():
    def __init__(self, size):
        self.surface = pygame.Surface(size)
        self.transparent_color = pygame.Color(74,65,42)
        self.surface.set_colorkey(self.transparent_color)

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
            self.__primary_surface.surface.fill(self.__primary_surface.transparent_color)
            
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

        