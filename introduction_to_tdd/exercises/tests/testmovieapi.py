import unittest
from unittest.mock import patch
import sys
sys.path.append("..")
from movieapi import movieapi as ma

class TestMovieApi(unittest.TestCase):


  def test_encodemoviename(self):
    self.assertEqual(ma.encodemoviename("STAR WARS"), "star%20wars")

  
  @patch('movieapi.movieapi.get_config')
  def test_get_config(self, mock_get_config):
    mock_get_config.return_value={
    "apikey": "12354",
    "url": "http://www.omdbapi.com/",
    "moviename": "Star Wars"
  }
    a = ma.mock_get("Star Wars")
    self.assertIsNotNone(a["apikey"])
    self.assertIsNotNone(a["url"])

  def test_buildurl(self):
    url = buildurl(ma.getconfig(movie_name))
    self.assertTrue(url.startswith("http"))

#  def test_hitapi(self):
#    pass


if __name__ == "__main__":
  unittest.main()
    #set environment variable with nonsense

  