-- Difficulty: easy
-- Problem: https://www.hackerrank.com/challenges/weather-observation-station-11/problem?isFullScreen=true

SELECT DISTINCT city
FROM station
WHERE (city NOT REGEXP "^[aeiou]") OR (city NOT REGEXP "[aeiou]$")
