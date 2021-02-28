import pygame, sys, time

pygame.init()

screen = pygame.display.set_mode([800,800])

my_surface = pygame.Surface([10,10])
my_surface.set_colorkey(pygame.Color("#ff0000"))
my_surface.fill(pygame.Color("#ff0000"))
pygame.draw.circle(my_surface, pygame.Color("#0000ff"), [5,5], 5)

location = [0,0]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("#ffffff")
    screen.blit(my_surface, location)
    location[0]+=10
    pygame.display.flip()
    time.sleep(.5)