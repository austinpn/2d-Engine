from random import randint
import unittest
import physics_engine.physics as physics
import physics_engine.vector as vector
from physics_engine.vector import Vector
from physics_engine.physics import PhysicsObject, Engine

class TestPhysicsObject(unittest.TestCase):
    def test_global_forces_default_zero(self):
        self.assertEqual(vector.get_inert_vector(2), PhysicsObject.get_global_force())
    
    def test_set_global_force(self):
        PhysicsObject.set_global_force([2,3])
        self.assertEqual(Vector(2,3), PhysicsObject.get_global_force())
        PhysicsObject.set_global_force(Vector(54,1.2))
        self.assertEqual(Vector(54, 1.2), PhysicsObject.get_global_force())
        PhysicsObject.set_global_force((0,0))
        self.assertEqual(Vector(0,0), PhysicsObject.get_global_force())

        PhysicsObject.set_global_force(Vector(54,1.2))
        phys_obj = PhysicsObject(0,0)
        self.assertEqual(Vector(54, 1.2), PhysicsObject.get_global_force())
        self.assertIsNot(PhysicsObject.get_global_force(),PhysicsObject.get_global_force())
    def test_physics_init(self):
        phys_obj = PhysicsObject([0,0], 0)
        self.assertIsInstance(phys_obj, PhysicsObject)
    
    def test_invalid_mass_zero_or_less_raises_ValueError(self):
        with self.assertRaises(ValueError):
            PhysicsObject(Vector(3,2), 0)
            PhysicsObject(Vector(3,2), -.002)
            PhysicsObject(Vector(3,2), -12412412)
    def test_invalid_location_raises_ValueError(self):
        with self.assertRaises(ValueError):
            PhysicsObject(Vector(3,2,0), 0)
            PhysicsObject(Vector(0,0,0), -.002)
            PhysicsObject(Vector(-2), -12412412)
            PhysicsObject([randint(-100,100) for x in range(1000)] , 100)

    def test_default_force_is_not_global_but_equals(self):
        phys_obj = PhysicsObject([0,0] , 1)
        self.assertEqual(PhysicsObject.get_global_force(), phys_obj.net_force)
        self.assertIsNot(PhysicsObject.get_global_force(), phys_obj.net_force)
    
    def test_mass(self):
        phys_obj = PhysicsObject([1,3], 1)
        self.assertEqual(phys_obj.mass, 1)
        phys_obj = phys_obj([5,2], 421)
        self.assertEqual(phys_obj.mass, 421)
        
    
    def test_force_exertion(self):
        phys_obj = PhysicsObject([0,0], 1)
        self.assertEqual(vector.get_inert_vector(2), phys_obj.applied_force)
        self.assertEqual(PhysicsObject.get_global_force(), phys_obj.net_force)
        phys_obj.apply_force([1,4])
        self.assertEqual(Vector(1,4), phys_obj.applied_force)
        self.assertEqual(Vector(1,4) + PhysicsObject.get_global_force(), phys_obj.net_force)
    
    def test_location(self):
        PhysicsObject.set_global_force([0,0])
        phys_obj = PhysicsObject((4,3) , 4)
        self.assertEqual(Vector(4,3), phys_obj.location)
        # self.assertFalse(phys_obj.in_motion)
        phys_obj.force_location(25,432)
        self.assertEqual(Vector(25, 432))
        # self.assertFalse(phys_obj.in_motion)
        for i in range(30):
            location = [randint(-1000,242), randint(1,320)]
            phys_obj.force_location(*location)
            self.assertEqual(Vector(*location), phys_obj.location)
    
    def test_initial_velecoity(self):
        PhysicsObject.set_global_force([0,0])
        phys_obj = PhysicsObject((4,3) , 4)
        self.assertFalse(phys_obj.in_motion)
        self.assertEqual(Vector(0,0), phys_obj.velocity)

        phys_obj = PhysicsObject([43,-231], 214)
        self.assertFalse(phys_obj.in_motion)
        self.assertEqual(Vector(0,0), phys_obj.velocity)

        phys_obj = PhysicsObject([1,1], 23, [0,0])
        self.assertFalse(phys_obj.in_motion)
        self.assertEqual(Vector(0,0), phys_obj.velocity)

        phys_obj = PhysicsObject([1,1], 23, [0,1])
        self.assertTrue(phys_obj.in_motion)
        self.assertEqual(Vector(0,1), phys_obj.velocity)

        phys_obj = PhysicsObject([1,1], 23, [32,0])
        self.assertTrue(phys_obj.in_motion)
        self.assertEqual(Vector(32,0), phys_obj.velocity)

    def test_motion_after_force(self):
        PhysicsObject.set_global_force([0,0])
        phys_obj = PhysicsObject([1,1], 23)
        self.assertFalse(phys_obj.in_motion)
        self.assertEqual(Vector(0,0), phys_obj.velocity)
        phys_obj.exert_force([3,2])
        self.assertTrue(phys_obj.in_motion)
        self.assertNotEqual(Vector(0,0), phys_obj.velocity)

        phys_obj = PhysicsObject([1,1], 23)
        self.assertFalse(phys_obj.in_motion)
        self.assertEqual(Vector(0,0), phys_obj.velocity, (0,0))
        phys_obj.exert_force([3,2])
        self.assertFalse(phys_obj.in_motion)
        self.assertEqual(Vector(0,0), phys_obj.velocity, (0,0))
        self.assertNotEqual(Vector(0,0), phys_obj.velocity)

class TestEngine(unittest.TestCase):
    def test_register_object(self):
        engine = Engine()
        self.assertEqual([], engine.registered_objects)
        to_register = [PhysicsObject([randint(0,300) , randint(-300, 0)] , randint(0,10)) for x in range(30)]
        engine.register(*to_register)
        self.assertEqual(to_register, engine.registered_objects)
        self.assertIsNot(to_register, engine.registered_objects)

    def test_kill_switch(self):
        engine = Engine()
        engine.run()
        self.assertTrue(engine.kill())
    def test_can_run_elsewhere_too(self):
        engine = Engine()
        to_register = [PhysicsObject([randint(0,300) , randint(-300, 0)] , randint(0,10)) for x in range(30)]
        engine.register(*to_register)
        engine.run()
        to_register.append(PhysicsObject([0,0], 1))
        engine.register(to_register[-1])
        self.assertEqual(to_register, engine.registered_obj)
        engine.kill()

if(__name__=="__main__"):
    unittest.main()