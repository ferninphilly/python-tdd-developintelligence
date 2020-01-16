import unittest
from unittest.mock import patch
import sys
sys.path.append("..")

import simple_maths.simple_maths as m


class TestSimpleMaths(unittest.TestCase):

  @patch('simple_maths.simple_maths.add', return_value=12)
  def test_add(self, add):
    #self.assertIsInstance(m.add(9,3), int)
    self.assertEqual(add(10,20),12)
  
  def test_subtract(self):
    self.assertEqual(m.subtract(10,3), 7)

  def test_multiply(self):
    self.assertEqual(m.multiply(5,6),30)

  def test_divide(self):
    self.assertEqual(m.divide(20,2), 10)

if __name__ == '__main__':
  unittest.main()