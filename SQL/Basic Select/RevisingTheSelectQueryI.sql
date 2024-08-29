-- Difficulty: easy
-- Problem:  https://www.hackerrank.com/challenges/revising-the-select-query/problem

SELECT *
FROM CITY
WHERE CountryCode = "USA" AND population > 100000
