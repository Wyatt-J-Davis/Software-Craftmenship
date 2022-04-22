import unittest

from fizzbuzzTDD import fizzbuzz_calculate 

class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_three(self):
        self.assertEqual(fizzbuzz_calculate(6), "Fizz")
    
    def test_has_three(self):
        self.assertEqual(fizzbuzz_calculate(13), "Fizz")

    def test_divisible_by_five(self):
        self.assertEqual(fizzbuzz_calculate(10), "Buzz")
    
    def test_has_5(self):
        self.assertEqual(fizzbuzz_calculate(5), "Fizz")
    
    def test_divisible_by_three_and_five(self):
        self.assertEqual(fizzbuzz_calculate(15), "FizzBuzz")

    def test_default(self):
        self.assertEqual(fizzbuzz_calculate(14), 14)

if __name__ == '__main__':
    unittest.main()