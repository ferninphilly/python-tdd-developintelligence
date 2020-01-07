import unittest
import sys
sys.path.append("..")
import mathsfuncs.mathsfuncs as m 

class TestMaths(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(m.add(5,7), 12)

  def test_subtract(self):
    self.assertEqual(m.subtract(10,5), 5)

  def test_multiply(self):
    self.assertEqual(m.multiply(10,5), 50)

  def test_divide(self):
    self.assertEqual(m.divide(10,5), 2)
    
if __name__ == '__main__':
  unittest.main()