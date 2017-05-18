import unittest

from my_adder import my_adder

class TestMyAdder (unittest.TestCase):

    def test_sum(self):
        a = 7
        b = 9
        self.assertTrue(a + b == my_adder(a, b))

if __name__ == '__main__':
     unittest.main()
