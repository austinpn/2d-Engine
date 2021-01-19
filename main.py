from pygamestuff import Graphics
from attributes import TriangleState , Physics
from time import sleep

width  = 600
height = 600
background = (2, 89, 171)

triSize = 20
triColor = 0
triWidth = 3
numTri = 10

graphics = Graphics(width , height , background)

graphics.initialize()
runtime = True


while runtime:
    runtime = graphics.quit()
    sleep(.033)
    graphics.redraw_game()
    graphics.pyupdate()
