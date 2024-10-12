-- Difficulty: medium
-- Problem: https://www.hackerrank.com/challenges/weather-observation-station-20/problem

SELECT 
    ROUND(AVG(LAT_N), 4)
FROM
(
    SELECT LAT_N, ROW_NUMBER() OVER (ORDER BY LAT_N) AS rn
    FROM station
) AS subq
WHERE rn = (SELECT CEIL((COUNT(rn)+1)/2) FROM station) OR
    rn = (SELECT FLOOR((COUNT(rn)+1)/2) FROM station)
