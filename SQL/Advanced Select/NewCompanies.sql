-- Difficulty: medium
-- Problem: https://www.hackerrank.com/challenges/the-company/problem

SELECT C.company_code, C.founder, COUNT(DISTINCT LM.lead_manager_code), COUNT(DISTINCT SM.senior_manager_code), COUNT(DISTINCT M.manager_code), COUNT(DISTINCT E.employee_code)
FROM Company AS C
JOIN Lead_Manager AS LM ON C.company_code = LM.company_code
JOIN Senior_Manager AS SM ON LM.lead_manager_code = SM.lead_manager_code
JOIN Manager AS M ON SM.senior_manager_code = M.senior_manager_code
JOIN Employee AS E ON M.manager_code = E.manager_code
GROUP BY C.company_code, C.founder
ORDER BY C.company_code ASC
