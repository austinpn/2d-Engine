import pygame

self._COLLISION = pygame.event.custom_type()
    
@property
def COLLISION(self):
    return self._COLLISION

def raise_collision(obja, objb):
    pygame.event.Event(COLLISION, obja=obja, objb=objb)
    return

