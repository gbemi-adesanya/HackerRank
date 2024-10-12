-- Difficulty: easy
-- Problem: https://www.hackerrank.com/challenges/asian-population/problem

SELECT SUM(CI.POPULATION)
FROM CITY AS CI JOIN COUNTRY AS CO ON CI.COUNTRYCODE = CO.CODE
WHERE CONTINENT = "Asia"
