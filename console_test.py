import time
import threading, multiprocessing

import pygame

from graphics.graphics_objects import Circle, PrimarySurface
from graphics.graphics_engine import Renderer
from physics.physics_objects import CirclePhysicsObject
from physics.physics_engine import Engine
from physics.vector import Vector



screen_size = [800,800]
base_surface = PrimarySurface(screen_size)
my_location = Vector(500, 500)

phys_obj = CirclePhysicsObject(my_location, 1, 5)
graph_obj = Circle(base_surface, my_location, 5)

phys_engine = Engine()
phys_engine.register_object(phys_obj)

renderer = Renderer(screen_size, base_surface)
renderer.register_object(graph_obj, 1)

# thread_lock = threading.Lock()

# renderer.run(thread_lock)
# phys_engine.run(thread_lock)

process_lock = multiprocessing.Lock()

renderer.run(process_lock)
phys_engine.run(process_lock)


# phys_obj.exert_force([-1,0])
run = True
while(run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                phys_obj.exert_force([-.05, 0])
            if event.key == pygame.K_d:
                phys_obj.exert_force([.05, 0])
            if event.key == pygame.K_w:
                phys_obj.exert_force([0, -.05])
            if event.key == pygame.K_s:
                phys_obj.exert_force([0, .05])
            
        
    time.sleep(.5)
phys_engine.kill()
renderer.kill()