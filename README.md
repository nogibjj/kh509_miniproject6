# Complex SQL Query for a MySQL Database
## Katelyn Hucker (kh509)

This is my project which uses MySQL Database to join and manipulate a database with a complex SQL Query. 
### Requirements:
- Design a complex SQL query involving joins, aggregation, and sorting
- Provide an explanation for what the query is doing and the expected results

### Explanation / How my code works:

The MySQL Database is a movies database which has genre, ratings, and movies. These tables have categories like genre name, title, genre id, release year, director, review_text, etc. The query *SELECTS* the movie title and then calculates the total rating score between multiple reviews. *FROM* movies the ratings table is *JOINED* on movie title/id. This puts the movies into 1 table. We then only want to look at movies released in year 2021. We *GROUP* the table by movie title and id then, *ORDER* by total score from highest to lowest. It then gives us the top five movies by score. 

### Checking the requirements

- JOIN: We join the tables at the very start of the database mp6.sql file.
- AGGREGATION: We sum and multiple by 10 to get a normalized total rating score
- SORTING: We sort the final database by table by highest to lowest score.

![image](https://github.com/nogibjj/kh509_miniproject6/assets/143521756/1b49e1f6-6f5d-49c9-95d2-a4c3c0c19e97)


### What we expect:
- Since we are only looking at movies in year 2021 we see that there is only 1 movie that would return: 'Movie B.' However typically we would see the top 5 movies in whatever year, and there would be multiple reviews contributing to the database so the aggregation actually works. 

