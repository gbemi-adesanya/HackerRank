-- Difficulty: easy
-- Problem: https://www.hackerrank.com/challenges/weather-observation-station-3/problem?isFullScreen=true

SELECT DISTINCT city
FROM station
WHERE ID % 2 = 0
