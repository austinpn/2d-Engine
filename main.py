from graphics import Graphics
from attributes import TriangleState , Physics
from time import sleep

width  = 1000
height = 700
background = (2, 89, 171)


graphics = Graphics(width , height , background)

graphics.initialize()
runtime = True


while runtime:
    runtime = graphics.quit()
    sleep(.033)
    graphics.redraw_game()
