-- Difficulty: easy
-- Problem: https://www.hackerrank.com/challenges/revising-the-select-query-2/problem

SELECT name
FROM City
WHERE CountryCode = "USA" AND population > 120000
