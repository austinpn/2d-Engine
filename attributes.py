import random
from assorted import vectorAddtion



class Physics():
    def __init__(self):
        pass
    def applyForce(self , location , velocity , forces):
        gravity = [0 , .3]
        forces.append(gravity)
        for force in forces:
            # print(velocity)
            vectorAddtion(velocity , force)
            # print(velocity)
        # print(velocity)
        

class TriangleState():
    def __init__(self , screenWidth , screenHeight , size , color , imageWidth = 0):
        # self.location = (screenWidth/2 , screenHeight/2)
        
        self.color = (color)
        self.location = [random.randrange(0 , screenWidth) , random.randrange(0 , screenHeight )]
        self.size = size
        self.shape = (self.location, [self.location[0] - size//3 , self.location[1] + size] , [self.location[0] + size//3 , self.location[1] + size] )
        self.width = imageWidth
        self.velocity = [0 , 0]
        self.thrust = [0 , 0]
    def updateLocation(self):
        self.location[0]+=self.velocity[0]
        print(self.location[1])
        self.location[1]+=self.velocity[1]
        print(self.location[1])
        print(self.velocity)
        # input()
        self.shape = [self.location , [self.location[0] - self.size/3 , self.location[1] + self.size] , [self.location[0] + self.size/3 , self.location[1] + self.size] ]
        # print(self.shape)