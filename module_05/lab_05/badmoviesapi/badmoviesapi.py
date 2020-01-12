from urllib import request, parse
import yaml
import json

#Here is where we load our creds from the credentials file
def get_credentials():
  configDrive='./config/configbadmovies.yaml'
  with open(configDrive, 'r') as creds:
    creds_obj=yaml.load(creds, Loader=yaml.BaseLoader)
  return creds_obj

#Here is where we get the input and urlencode the movie name
def url_encode_moviename(movie_name):
  return parse.quote(movie_name.lower())

#Create the URL to hit the omdb api
def create_url(movie_name):
  creds = get_credentials()
  creds['moviename']=url_encode_moviename(movie_name)
  return "{baseapiurl}?{apikey}&t={moviename}".format(**creds)

#Here's where we hit the api and get data back
def hit_omdb_api(url):
  req = request.Request(url)
  resp = request.urlopen(req).read()
  return json.loads(resp.decode('utf-8'))
  
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

def get_avg_score(movie_name):
  url=create_url(movie_name)
  movieinfo=hit_omdb_api(url)
  ratings=get_ratings_system(movieinfo)
  return "{0:.2f}".format(ratings)

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
