import unittest

from app.values.FizzBuzz import fizzBuzz, fizzBuzzOfNNumbers


class FizzBuzzTest(unittest.TestCase):

    '''
    Test case to is the multiple of 3 returns Fizz
    '''
    def testIsMultiplesOf3ReturnFizz(self):
        self.assertEqual(fizzBuzz(3), "Fizz")
        self.assertEqual(fizzBuzz(9), "Fizz")
        self.assertEqual(fizzBuzz(18), "Fizz")
        self.assertEqual(fizzBuzz(21), "Fizz")
        self.assertEqual(fizzBuzz(-3), "Fizz")

    '''
       Test case to is the multiple of 5 returns Buzz 
    '''
    def testIsMultiplesOf5ReturnBuzz(self):
        self.assertEqual(fizzBuzz(-5), "Buzz")
        self.assertEqual(fizzBuzz(25), "Buzz")
        self.assertEqual(fizzBuzz(10), "Buzz")
        self.assertEqual(fizzBuzz(100), "Buzz")

    '''
       Test case to is the multiple of 15 returns FizzBuzz
    '''
    def testIsMultiplesOf3And5ReturnFizzBuzz(self):
        self.assertEqual(fizzBuzz(-45), "FizzBuzz")
        self.assertEqual(fizzBuzz(30), "FizzBuzz")
        self.assertEqual(fizzBuzz(60), "FizzBuzz")
        self.assertEqual(fizzBuzz(15), "FizzBuzz")
        self.assertEqual(fizzBuzz(15), "FizzBuzz")

    '''
       Test case whether the number is not divisble by 3 or 5 or 15 returns nmuber itself or not 
    '''
    def testIsNumberNotDivisible3_5_15ReturnsNumber(self):
        self.assertEqual(fizzBuzz(-4), "-4")
        self.assertEqual(fizzBuzz(8), "8")
        self.assertEqual(fizzBuzz(17), "17")
        self.assertEqual(fizzBuzz(31), "31")

    '''
    This is a negative test case and will fail 
    '''
    def testNegativeCaseForStringNumber(self):
        self.assertEquals(fizzBuzz("2"),"2")

    def testCheckForFloatNumber(self):
        self.assertEquals(fizzBuzz(int(2.1)), "2")

    def testfizzBuzzOfNNumbers(self):
        expectedEncodedData = ['1','2',"Fizz",'4',"Buzz"]
        actualEncodedData = fizzBuzzOfNNumbers(1,5)
        print(actualEncodedData)
        self.assertEqual(actualEncodedData, expectedEncodedData)
if __name__ == '__main__':
    unittest.main()
