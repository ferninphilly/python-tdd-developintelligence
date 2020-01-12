import json

def handler(event, context):
    print("Oh Hai Mark!")
    print("Received event: " + json.dumps(event["queryStringParameters"], indent=2))
    return {
  "statusCode": 200,
  "isBase64Encoded": False,
  "headers": {},
  "body": "42"
}