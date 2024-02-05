# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangles(self):
        self.assertEqual(classifyTriangle(3,4,3), 'Isoceles', '3,4,3 is an Isoceles triangle')

    def testBounds1(self):
        self.assertEqual(classifyTriangle(201, 201, 201), 'InvalidInput', '201,201,201 is invalid')
        
    def testBounds2(self):
        self.assertEqual(classifyTriangle(-1, 10, 10), 'InvalidInput', '-1,10,10 is invalid')
    
    def isTriangle(self):
        self.assertEqual(classifyTriangle(10,2,3), 'NotATriangle', '10,2,3 is not a triangle')

    def validInputs1(self):
        self.assertEqual(classifyTriangle('A','A','A'), 'InvalidInput', 'A,A,A is not valid input')
    
    def validInputs2(self):
        self.assertEqual(classifyTriangle(1.0,2.065,45.999), 'InvalidInput', 'Floats are not valid input')
    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

