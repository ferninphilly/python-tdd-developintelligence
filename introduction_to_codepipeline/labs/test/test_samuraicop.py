import unittest
import sys

class TestSamuraiCop(unittest.TestCase):
  
  def setUp(self):
    sys.path.append("../samuraicops")
    from samuraicops.SamuraiCop import SamuraiCop
    self.samurai = SamuraiCop("Joe",
    ["Fujiyama", "Okamura", "Henchman1", 
    "Henchman2","HenchWoman", "Shotgun Guy", 
    "Burning Van Driver"])

  #We are going to test the instantation, the length of lists,
  #and the strings functions
  def test_bad_guys_beaten_up(self):
    self.assertEqual(self.samurai.name, "Joe")
    self.assertIsInstance(self.samurai.badguys, list)
    self.assertEqual(len(self.samurai.badguys), 7)
    self.assertIn("Okamura", self.samurai.badguys)
    badguy = self.samurai.bad_guys_beaten_up()
    self.assertEqual(badguy, "Burning Van Driver")
    
  #Test to check if the bool goes true to false to true
  def test_you_are_fired(self):
    self.assertTrue(self.samurai.cop)
    self.samurai.you_are_fired()
    self.assertFalse(self.samurai.cop)

  def test_birthday_chickens_killed(self):
    self.assertEqual(self.samurai.chickens, 0)
    self.samurai.birthday_chickens_killed()
    self.assertGreater(self.samurai.chickens,0)
    
if __name__ == '__main__':
  unittest.main()