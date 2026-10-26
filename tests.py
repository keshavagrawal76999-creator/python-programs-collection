import unittest
from main import factorial, fibonacci, is_prime, is_palindrome

class ProgramTests(unittest.TestCase):
    def test_factorial(self): self.assertEqual(factorial(5), 120)
    def test_fibonacci(self): self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
    def test_prime(self): self.assertTrue(is_prime(13)); self.assertFalse(is_prime(1))
    def test_palindrome(self): self.assertTrue(is_palindrome("Never odd or even"))

if __name__ == "__main__": unittest.main()
