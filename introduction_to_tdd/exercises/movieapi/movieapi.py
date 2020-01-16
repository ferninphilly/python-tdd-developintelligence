from urllib.parse import quote
import requests
import json
import os

def encodemoviename(movie_name):
  return quote(movie_name.lower())

def getconfig():
  cfg = {
    "apikey": os.getenv("APIKEY"),
    "url": os.getenv("URL"),
  }
  return cfg

def buildurl(movie_name):
 a = getconfig()
 a["moviename"] = encodemoviename(movie_name)
 return "{url}/?{apikey}&t={moviename}".format(**cfg)

#Here's where we hit the api and get data back
def run_request(url):
  api_response = requests.get(url)
  if api_response.ok:
    return json.loads(api_response.content.decode('utf-8'))
  else:
    return None

#Here is how we will translate IMDB ratings to an out of 100 scale  
def _imdb_balancer(rating):
  rate = rating[:-3]
  return float(rate) * 10

def _rotten_tomatoes_balancer(rating):
  return float(rating[:-1])

def _metacritic_balancer(rating):
  return float(rating[:-4])

#Create Ratings system
def get_ratings_system(movie_info):
  all_rtngs = []
  for rating in movie_info["Ratings"]:
    if rating["Source"] == "Internet Movie Database":
      all_rtngs.append(_imdb_balancer(rating["Value"]))
    if rating["Source"] == "Rotten Tomatoes":
      all_rtngs.append(_rotten_tomatoes_balancer(rating["Value"]))
    if rating["Source"] == "Metacritic":
      all_rtngs.append(_metacritic_balancer(rating["Value"]))
  return sum(all_rtngs) / len(all_rtngs)

def get_avg_score(movie_data):
  ratings=get_ratings_system(movie_data)
  return "{0:.2f}".format(ratings)

def get_director(movie_data):
  return movie_data.get("Director")  

def get_run_time(movie_data):
  return movie_data.get("Runtime")

def return_bad_movie(movie_name):
  creds = get_config() 
  print(creds)
  url = build_url(creds, movie_name)
  movie_data = run_request(url)
  print(movie_data)
  return get_avg_score(movie_data)

def handler(event, context):
  movie_name = event["queryStringParameters"]["moviename"]
  nmbr = return_bad_movie(movie_name)
  return {
    "statusCode": 200,
    "isBase64Encoded": False,
    "headers": {},
    "body": nmbr
  }