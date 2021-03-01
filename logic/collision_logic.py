from ..physics_objects import WallType

def ball_and_wall(ball, wall_type):
    """ 
    Flips velocity and force
    """
    if(WallType == WallType.LEFT or WallType == WallType.RIGHT):
        ball.location[0] *=-1
    else:
        ball.location[1] *=-1