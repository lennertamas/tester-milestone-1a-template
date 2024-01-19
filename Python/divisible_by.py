#Find numbers which are divisible by given number**

#Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. 
#First argument is an array of numbers and the second is the divisor.

#Example(Input1, Input2 --> Output)**

#You have to implement the prepared divisible by method which has two argument. 
#The first is the list of numbers, the second one is the divisor number. 
#Select the elements from the list that can be divided by the divisor and return them in a new list.

#e.g.: 
#([1,2,3,4,5,6], 2)  -> [2,4,6]
#([1,2,3,4,5,6], 2), -> [2,4,6]
#([1,2,3,4,5,6], 3), -> [3,6]

import unittest

def divisible_by(numbers, divisor):
    #code to implement
    pass









# AUTOMATED TEST, DO NOT MODIFIED
class TestStringMethods(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(divisible_by([1,2,3,4,5,6], 2), [2,4,6])
        self.assertEqual(divisible_by([1,2,3,4,5,6], 3), [3,6])
        self.assertEqual(divisible_by([0,1,2,3,4,5,6], 4), [0,4])
        self.assertEqual(divisible_by([0], 4), [0])
        self.assertEqual(divisible_by([1,3,5], 2), [])
        self.assertEqual(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 1), [0,1,2,3,4,5,6,7,8,9,10])


unittest.main()

