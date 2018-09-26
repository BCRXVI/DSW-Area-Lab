import math #lets us use the math module.
import unittest #unittest module helps us test small sections of code

def circleArea(radius): 
    return radius * radius *math.pi

def rectArea(base, height):
    if base<0 or height<0:    
        return-1
    return base * height

def trapArea(base1, base2, height):
    return height *(base1 + base2) / 2

def triArea(base,height):
    return base * height / 2
    
class MyTest(unittest.TestCase): #using TestCase class from unittest module.
    def testCircleArea(self):
        """returns the are of a circle with the given radius"""
        self.assertEqual(circleArea(5), 25*math.pi)
        self.assertAlmostEqual(circleArea(3.25), 3.25*3.25*math.pi)
    def testRectArea(self):
        """Returns the base and height"""
        self.assertEqual(rectArea(-3,-2),-1)
        self.assertAlmostEqual(rectArea(6,2),12)
    def testTrapArea(self):
        """ """
        self.assertEqual(trapArea(50,2,1),26)
        self.assertAlmostEqual(trapArea(6,4,3),15)
    def testTriArea(self):
        self.assertEqual(triArea(3,20),3*20/2)
        self.assertAlmostEqual(triArea(19,6),19*6/2)
                
        #Formula of a circle :radius * radius* PI
        #Formula of a rectangle: base * height
        #Formula of a trapezoid: height *   (base1 + base2) / 2
        #Formula of a triangle: base *  height / 2