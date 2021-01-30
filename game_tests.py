import unittest
from physics import Velocity

class TestPhysics(unittest.TestCase):
    def test_mobile(self):
        vel = Velocity(1,0,1)
        self.assertEqual(2, vel._Velocity__num_nonzero)
        self.assertTrue(vel.is_mobile)
    
    def test_immobile(self):
        vel = Velocity(0,0)
        self.assertEqual(0, vel._Velocity__num_nonzero)
        self.assertFalse(vel.is_mobile)
    
    def test_change_val(self):
        vel = Velocity(0,0,0)
        self.assertFalse(vel.is_mobile)
        vel[1]+=3
        self.assertTrue(vel.is_mobile)
        vel[1]-=3
        self.assertFalse(vel.is_mobile)

    def test_sum(self):
        vel_a = Velocity(1,0)
        vel_b = Velocity(0,1)
        vel_a_plus_b = Velocity.sum(vel_a , vel_b)
        self.assertEqual(vel_a_plus_b[0] , 1)
        self.assertEqual(vel_a_plus_b[1] , 1)

    def test_mult(self):
        vect = Velocity(1,2,3,4)
        vect.multiply(2)
        self.assertEqual([2,4,6,8], list(vect))
        new_vect = vect*.5
        self.assertEqual([1,2,3,4], list(new_vect))
        newer_vect = 2*new_vect
        self.assertEqual([2,4,6,8], list(newer_vect))

if __name__ == "__main__":
    unittest.main()