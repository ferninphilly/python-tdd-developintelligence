import requests


def handler(event, context):
  nmbr = requests.get("https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg")
  return {
    "statusCode": 200,
    "isBase64Encoded": False,
    "headers": {},
    "body": nmbr
  }
