# TDD Exercise ONE

## Your Task

As we talked about in the previous modules- TDD and most of the work around it comes down to one word: **planning**. For the next 45 minutes I want everyone here to **plan out** and **create** an application that does the following:

1. Takes, as an input, the name of a film
2. Using the name of that film it then hits the OMDB movie database API
3. The OMDB API is going to return an ARRAY to you of reviews from different sources
4. Take those reviews and get an average for all of them (remember that you will have to create scale)
5. Present the average score _as well as_ the poster to the user
6. Profit!

## PLAN!

1. Your first job is to break this down into functions. Think about what you have to do. 
2. _Resist the urge_ to jump into code. We're going to do this via TDD. This is what we ultimately want our coders doing as well. 
3. Name your functions and their expected return values.
4. Submit your plans for discussion.
5. Use config files (best practice)

## Required data

1. Here is the API key: **dd070ac3**
2. Here is the base URL: **http://www.omdbapi.com/**

## Sample return data:

```json
{
Title: "Star Wars: Episode IV - A New Hope",
Year: "1977",
Rated: "PG",
Released: "25 May 1977",
Runtime: "121 min",
Genre: "Action, Adventure, Fantasy, Sci-Fi",
Director: "George Lucas",
Writer: "George Lucas",
Actors: "Mark Hamill, Harrison Ford, Carrie Fisher, Peter Cushing",
Plot: "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader.",
Language: "English",
Country: "USA",
Awards: "Won 6 Oscars. Another 52 wins & 28 nominations.",
Poster: "https://m.media-amazon.com/images/M/MV5BNzVlY2MwMjktM2E4OS00Y2Y3LWE3ZjctYzhkZGM3YzA1ZWM2XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
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
],
Metascore: "90",
imdbRating: "8.6",
imdbVotes: "1,164,199",
imdbID: "tt0076759",
Type: "movie",
DVD: "21 Sep 2004",
BoxOffice: "N/A",
Production: "20th Century Fox",
Website: "N/A",
Response: "True"
}
```

## Deliverables:

Make a plan (if you can) of what each function will look like. We'll share this plan with the class and the group. *Talk through each step*. 
REALLY try to understand what you want to do and what you are trying to achieve! 
BEFORE we are ready to code we should have our tests written!