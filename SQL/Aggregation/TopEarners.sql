-- Difficulty: easy
-- Problem: https://www.hackerrank.com/challenges/earnings-of-employees/problem

SELECT MAX(earnings), COUNT(*)
FROM
    (SELECT employee_id, (salary * months)  as earnings
     FROM Employee) as E
WHERE earnings = (SELECT MAX(months * salary) FROM Employee);
