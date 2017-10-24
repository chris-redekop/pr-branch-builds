import unittest
from Calculator import Calculator

class MyTestCase(unittest.TestCase):
  def test_default_sum_set(self):
    hw = Calculator()
    self.assertEqual(hw.sum, 10)

if __name__ == '__main__':
  unittest.main()
