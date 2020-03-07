from attributes import Physics
testvel = [0 , 0]
forces = [[0 , 0]]

for x in range(100):
    Physics.applyForce(testvel , testvel , forces , 0)
print(testvel)