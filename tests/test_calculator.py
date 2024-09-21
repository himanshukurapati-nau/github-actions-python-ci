import unittest
from src.calculator import add, subtract, divide 
class TestCalculator(unittest.TestCase):
   def test_add(self):
    self.assertEqual(add(2, 3), 5)
    self.assertEqual(add(-1, 1), 0)
    self.assertEqual(add(-1, -1), -2)
def test_subtract(self):
  # COMPLETE HERE
  self.assertEqual(subtract(10,6), 4)
  self.assertEqual(subtract(-5, 3), -8)
  self.assertEqual(subtract(0, 10), -10)
def test_divide(self):
  # COMPLETE HERE
  self.assertEqual(divide(10,2), 5)
  self.assertEqual(divide(-15,3), -5)
  self.assertEqual(divide(10,0), "Error: Division by zero")

if __name__ == '__main__':
   unittest.main()