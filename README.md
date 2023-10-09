### Requirements:
- Design a complex SQL query involving joins, aggregation, and sorting
- Provide an explanation for what the query is doing and the expected results

### Explanation / How my code works:

The MySQL Database is a movies database which has genre, ratings, and movies. These tables have categories like genre name, title, genre id, release year, director, review_text, etc. The query *SELECTS* the movie title and then calculates the total rating score between multiple reviews. *FROM* movies the ratings table is *JOINED* on movie title/id. This puts the movies into 1 table. We then only want to look at movies released in year 2021. We *GROUP* the table by movie title and id then, *ORDER* by total score from highest to lowest. It then gives us the top five movies by score. 

### Checking the requirements

- JOIN: We join the tables at the very start of the database mp6.sql file.
- AGGREGATION: We sum and multiple by 10 to get a normalized total rating score
- SORTING: We sort the final database by table by highest to lowest score.


### What we expect:
- Since we are only looking at movies in year 2021 we see that there is only 1 movie that would return: 'Movie B.' However typically we would see the top 5 movies in whatever year, and there would be multiple reviews contributing to the database so the aggregation actually works. 
