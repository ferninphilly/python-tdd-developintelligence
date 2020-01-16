# Break this down into steps

1. Ingest name of movie. (example: "STAR Wars")
2. URLENCODE name of movie (example: "star%20wars")
3. Make api connection
  - get api key (config file?)ß
  - build the url ("http://whatever?apikey=myapi/title=star%20wars")
  - Run GET request against URL
4. Array receiver -> transform to dictionary (example: 
```json
Ratings: [
{
Source: "Internet Movie Database",
Value: "8.6/10"
},
{
Source: "Rotten Tomatoes",
Value: "93%"
},
{
Source: "Metacritic",
Value: "90/100"
}
  ]
```,)

5. Transform each value to the same scale (/100)

6. Make sure all data is in float format

7. Average the values together

8. Return avg to user.