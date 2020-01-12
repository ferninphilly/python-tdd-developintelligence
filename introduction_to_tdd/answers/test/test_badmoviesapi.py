import unittest
from unittest.mock import patch
import json
import sys
sys.path.append("..")
from badmoviesapi.badmoviesapi import get_director, get_run_time, get_config, build_url, run_request, get_avg_score


FAKE_DATA = {'Title': 'Troll 2', 'Year': '1990', 'Rated': 'PG-13', 'Released': '12 Oct 1990', 
'Runtime': '95 min', 'Director': 'Claudio Fragasso', 'Actors': 'Michael Paul Stephenson, George Hardy, Margo Prey, Connie Young', 
'Ratings': [ {'Source': 'Internet Movie Database', 'Value': '2.9/10'}, {'Source': 'Rotten Tomatoes', 'Value': '6%'}], 
'Metascore': 'N/A' }

class TestBadMovies(unittest.TestCase):
  
  def setUp(self):
    self.cfg = get_config("./test_config.yaml")

  def test_get_config(self):
    self.assertIn("baseapiurl", self.cfg)
    self.assertIn("apikey", self.cfg)

  def test_build_url(self):
    url = build_url(self.cfg, "Troll 2")
    self.assertTrue(url.endswith("troll%202"))
    self.assertTrue(url.startswith("http://"))

  #Here is our mock function- we are going to replace the meaning of a function
  @patch('badmoviesapi.badmoviesapi.requests.get')
  def test_run_request(self, mock_get):
    #Here I'm telling the system to override the "requests.get" method with a fake "mock_get" method
    mock_get.return_value.content = json.dumps(FAKE_DATA).encode()
    resp = run_request("Troll 2")
    self.assertEqual(resp["Director"], "Claudio Fragasso")
    self.assertEqual(resp["Runtime"], "95 min")
    self.assertIn("Title", resp)

  def test_get_avg_score(self):
    scores = get_avg_score(FAKE_DATA)
    self.assertEqual(scores, "17.50")

  def test_get_run_time(self):
    runtime = get_run_time(FAKE_DATA)
    self.assertIsNotNone(runtime)

  def test_get_director(self):
    director = get_director(FAKE_DATA)
    self.assertIsNotNone(director)

if __name__ == '__main__':
  unittest.main()