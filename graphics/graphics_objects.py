from enum import Enum
import time
import threading, multiprocessing
from pygame import Surface, Color, draw




class Renderable():
    def render(self):
        pass

class GraphicsObject(Renderable):
    transparent_color = Color(74,65,42)
    def __init__(self, parent_obj, location, width, height, load_img=False):
        super().__init__()
        self.location = location
        self.has_img = load_img
        self.parent_surface = parent_obj.surface
        
        self.surface = Surface([width, height])
        self.surface.set_colorkey(self.transparent_color)
        self.surface.fill(self.transparent_color)


class Circle(GraphicsObject):
    def __init__(self, parent_obj, location, radius, load_img=False):
        super().__init__(parent_obj, location, radius*2, radius*2, load_img)
        self.radius = radius
        draw.circle(self.surface, Color("#2931b3"), [self.radius,self.radius], self.radius)
    def render(self):
        self.parent_surface.blit(self.surface, self.location)


class PrimarySurface():
    def __init__(self, size):
        self.surface = Surface(size)
        self.transparent_color = Color(74,65,42)
        self.surface.set_colorkey(self.transparent_color)

        