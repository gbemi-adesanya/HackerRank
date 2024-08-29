-- Difficulty: easy
-- Problem: https://www.hackerrank.com/challenges/weather-observation-station-5/problem

WITH secondary AS (
    SELECT city, LENGTH(CITY) as len
    FROM station
    ORDER BY LENGTH(city), city
    
), min_city AS (
    SELECT city, len
    from secondary
    ORDER BY len, city
    LIMIT 1
    
), max_city AS (
    SELECT city, len
    from secondary
    ORDER BY len DESC, city 
    LIMIT 1
)

SELECT city, len
FROM min_city
  
UNION
  
SELECT city, len
FROM max_city
