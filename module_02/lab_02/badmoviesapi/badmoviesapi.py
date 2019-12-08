import yaml
import json
import requests
from urllib.parse import quote

def get_config(config_file):
  with open(config_file) as f:
    cfg = yaml.load(f, Loader=yaml.FullLoader)
  return cfg

def build_url(cfg, movie_name):
  moviename_encoded = quote(movie_name)
  return cfg["baseurl"] + cfg["apikey"] + "&t=" + moviename_encoded

def run_request(url):
  api_response = requests.get(url)
  if api_response.ok:
    return json.loads(api_response.content.decode('utf-8'))
  else:
    return None

#Return the ratings
def get_scores(sources):
  if sources["Metascore"] == "N/A":
    for source in sources["Ratings"]:
      if source["Source"] == "Rotten Tomatoes":
        return source
      if source["Source"] == "Internet Movie Database":
        return source
  return {"Source": "Metascore", "Value": sources["Metascore"]}

def get_run_time(movie_data):
  return movie_data.get("Runtime")

def get_director(movie_data):
  return movie_data.get("Director")    

if __name__ == '__main__':
  filmname = input("Enter a film name: ")
  cfg = get_config("config.yaml")
  url = build_url(cfg, filmname)
  resp = run_request(url)
  director = get_director(resp)
  runtime = get_run_time(resp)
  scores = get_scores(resp)
  print(filmname + " was directed by " + director + ".\n")
  print(filmname + " has a run time of " + runtime + ".\n")
  print(filmname + " has a rating of " + scores.get("Value") + " according to " + scores.get("Source"))
