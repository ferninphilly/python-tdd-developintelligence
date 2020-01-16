import requests
from urllib.parse import quote
import os
import yaml
import json

def get_config():
  """
  get_config takes no input but will decide where the inputs come from
  returns a dictionary that contains the credentials that we'll use to build the url
  """
  if os.environ["ENV"] != "prod":
    with open('./config/configbadmovies.yaml', 'r') as creds:
      creds_obj=yaml.load(creds, Loader=yaml.BaseLoader)
    return creds_obj
  else:
    creds_obj=dict()
    creds_obj['baseapiurl'] = os.environ["API_URL"]
    creds_obj['apikey'] = os.environ["API_KEY"]
  return creds_obj 
#Here is where we get the input and urlencode the movie name
def url_encode_moviename(movie_name):
  return quote(movie_name.lower())

#Create the URL to hit the omdb api
def build_url(creds, movie_name):
  creds['moviename']=movie_name 
  #url_encode_moviename(movie_name)
  return "{baseapiurl}?{apikey}&t={moviename}".format(**creds)


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

