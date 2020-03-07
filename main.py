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

# triangle = TriangleState(width , height , triSize , triColor)
triangles = []

for i in range(numTri):

    triangles.append(TriangleState(width , height , triSize , triColor))
# graphics.drawPolygon(triangle.color , triangle.shape , triangle.width)

graphics.drawPolygonArr(triangles)

graphics.pyupdate()


while runtime:
    runtime = graphics.quit()
    sleep(.033)
    for triangle in triangles:
        print(triangle.velocity)
        Physics.applyForce(triangle.location , triangle.velocity , triangle.thrust)
        triangle.updateLocation()
    graphics.drawPolygonArr(triangles)
    graphics.pyupdate()
