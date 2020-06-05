import unittest

from app.values.FizzBuzz import fizzBuzz

class FizzBuzzTest(unittest.TestCase):

    def testIsMultiplesOf3ReturnFizz(self):
        self.assertEqual(fizzBuzz(3), "Fizz")
        self.assertEqual(fizzBuzz(9), "Fizz")
        self.assertEqual(fizzBuzz(18), "Fizz")
        self.assertEqual(fizzBuzz(21), "Fizz")
        self.assertEqual(fizzBuzz(-3), "Fizz")

    def testIsMultiplesOf5ReturnBuzz(self):
        self.assertEqual(fizzBuzz(-5), "Buzz")
        self.assertEqual(fizzBuzz(25), "Buzz")
        self.assertEqual(fizzBuzz(10), "Buzz")
        self.assertEqual(fizzBuzz(100), "Buzz")

    def testIsMultiplesOf3And5ReturnFizzBuzz(self):
        self.assertEqual(fizzBuzz(-45), "FizzBuzz")
        self.assertEqual(fizzBuzz(30), "FizzBuzz")
        self.assertEqual(fizzBuzz(60), "FizzBuzz")
        self.assertEqual(fizzBuzz(15), "FizzBuzz")

    def testIsNumberNotDivisible3_5_15ReturnsNumber(self):
        self.assertEqual(fizzBuzz(-4), "-4")
        self.assertEqual(fizzBuzz(8), "8")
        self.assertEqual(fizzBuzz(17), "17")
        self.assertEqual(fizzBuzz(31), "31")

if __name__ == '__main__':
    unittest.main()
