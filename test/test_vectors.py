import unittest
import random
import physics_engine.vector as vector
from physics_engine.vector import Vector
import physics_engine.physics as physics
from physics_engine.physics import PhysicsObject

class TestVectors(unittest.TestCase):
    def test_vectors_can_be_empty(self):
        vectorA = Vector()
    
    def test_equality_operator(self):
        vectorA = Vector(1,2,3)
        vectorB = Vector(1,2,3)
        vectorC = Vector(2,1,3)
        vectorD = Vector(32,12,4)
        vectorE = Vector(1,2)
        self.assertIsNot(vectorA, vectorB)
        self.assertEqual(vectorA, vectorB)
        self.assertEqual(list(vectorA), [1,2,3])
        self.assertNotEqual(vectorA, vectorC)
        self.assertNotEqual(vectorB, vectorC)
        self.assertNotEqual(vectorA, vectorE)

        self.assertNotEqual(vectorA, [1,2,3])
        self.assertNotEqual(vectorA*2, [2,4,6])
    def test_equivalent_vectors_are_equal(self):
        vectorA = Vector(1,2,3)
        vectorB = Vector(1,2,3)
        self.assertEqual(vectorA,vectorB)

        randArr = [random.randint(-100,100) for x in range(10)]
        vectorC = Vector(*randArr)
        vectorD = Vector(*randArr)
        self.assertEqual(vectorA,vectorB)
    def test_different_valued_vectors_are_not_equal(self):
        vectorA = Vector(7,6,2,3)
        vectorB = Vector(2,34,4,1000)
        self.assertNotEqual(vectorA, vectorB)

        vectorC = Vector(1,1,1,1,1,1,1)
        vectorD = Vector(1,1,1,1)
        self.assertNotEqual(vectorC, vectorD)
    def test_summation_creates_new_objects(self):
        vectorA = Vector(1,2,3)
        vectorB = Vector(10,10,-1)
        vectorC = vectorA + vectorB
        self.assertIsNot(vectorA, vectorC)
        self.assertIsNot(vectorB, vectorC)
        self.assertIsInstance(vectorA, Vector)
        self.assertIsInstance(vectorB, Vector)
        self.assertIsInstance(vectorC, Vector)
    def test_summation_adds_well_like_addition(self):
        vectorC = Vector(1,2,3) + Vector(10,10,-1)
        self.assertEqual(list(vectorC) , [11,12,2])
        self.assertEqual(vectorC, Vector(11,12,2))
        self.assertIsInstance(vectorC, Vector)
    def test_vector_dimension(self):
        vectorA = Vector(5,2,3,5)
        self.assertEqual(4, vectorA.dimension)
        self.assertEqual(4, len(vectorA))

        vectorA = Vector()
        self.assertEqual(0, vectorA.dimension)
        self.assertEqual(0, len(vectorA))
    def test_vector_constant_mult(self):
        vectorA = Vector(1,2,3)
        vectorB = vectorA*2
        self.assertIsNot(vectorA , vectorB)
        self.assertEqual(list(vectorB) , [2,4,6])

        vectorC = 2*vectorA
        self.assertIsNot(vectorA, vectorC)
        self.assertIsNot(vectorB, vectorC)
        self.assertEqual(list(vectorC), [2,4,6])
        self.assertEqual(vectorC, vectorB)

        self.assertIsInstance(vectorA, Vector)
        self.assertIsInstance(vectorB, Vector)
        self.assertIsInstance(vectorC, Vector)
    def test_update_should_update(self):
        vectorA = Vector(1,2,3)
        vectorB = vectorA
        vectorB.update([3,4,5])
        self.assertIsInstance(vectorA, Vector)
        self.assertEqual(list(vectorB), [3,4,5])
        self.assertIs(vectorA, vectorB)
    def test_get_item_at_index(self):
        vectorA = Vector(1,2,3,4)
        self.assertEqual(1, vectorA[0])
        self.assertEqual(2, vectorA[1])
        self.assertEqual(3, vectorA[2])
        self.assertEqual(4, vectorA[3])
        self.assertEqual(4, vectorA[-1])
        self.assertEqual(3, vectorA[2])
        for val in vectorA:
            self.assertIsInstance(val, float)
    def test_set_vector_at_index(self):
        vectorA = Vector(1,2,3,4,5)
        vectorA[3] = -1
        self.assertEqual(-1, vectorA[3])
        self.assertEqual(list(vectorA), [1,2,3,-1,5])
        vectorA[-1]+=4
        self.assertEqual(9, vectorA[4])
        self.assertEqual(list(vectorA) , [1,2,3,-1,9])
        for val in vectorA:
            self.assertIsInstance(val, float)
    def test_inert_property(self):
        vectorA = Vector(1,0,9,1)
        self.assertFalse(vectorA.inert)
        vectorA = Vector(0,0)
        self.assertTrue(vectorA.inert)
        vectorA = Vector(7,357,123,6,-32)
        self.assertFalse(vectorA.inert)
        vectorA[0]+=-7
        self.assertFalse(vectorA.inert)
        vectorA[1] = 0
        self.assertFalse(vectorA.inert)
        vectorA[2] = 0
        self.assertFalse(vectorA.inert)
        vectorA[3]-=6
        self.assertFalse(vectorA.inert)
        vectorA[4]+=32
        self.assertTrue(vectorA.inert)

        vectorA[2]+=1
        self.assertFalse(vectorA.inert)
    def test_get_inert_vector(self):
        vectorA = vector.get_inert_vector(3)
        self.assertEqual([0]*3, list(vectorA))
        self.assertEqual(3, vectorA.dimension)
        self.assertTrue(vectorA.inert)

if(__name__=='__main__'):
    unittest.main()
