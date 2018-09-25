import math #lets us use the math module.
import unittest #unittest module helps us test small sections of code

def circleArea(radius): 
    return radius * radius *math.pi

def rectArea(base, height):
    return 1

def trapArea(base1, base2, height):
    return 1

def triArea(base,height):
    return 1
    
	
class MyTest(unittest.TestCase): #using TestCase class from unittest module.
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25*math.pi)
        self.assertAlmostEqual(circleArea(3.25),*math.pi)
    def testRectArea(self):
        selfassertEqual(rectArea(50,2),100)
        selfassertEqual(rectArea(6,2),18)
    def testTrapArea(self):
        selfassertEqual(trapArea(3,3), 6)
        selfassertEqual(trapArea(10))
    def testTriArea(self):
        selfassertEqual(triArea(5), 25*math.pi
        selfassertEqual(triAre(10), 100*math.pi