-- Difficulty: easy
-- Problem: https://www.hackerrank.com/challenges/the-blunder/problem

SELECT CEIL(AVG(salary - REPLACE(salary, "0", "")))
FROM EMPLOYEES
