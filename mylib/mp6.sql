SELECT 
    m.movie_id,
    m.title AS movie_title,
    SUM(r.rating * 10) AS total_rating_score
FROM
    movies m
JOIN
    ratings r ON m.movie_id = r.movie_id
WHERE
    YEAR(m.release_year) = 2021
GROUP BY
    m.movie_id, m.title
ORDER BY
    total_rating_score DESC
LIMIT 5;