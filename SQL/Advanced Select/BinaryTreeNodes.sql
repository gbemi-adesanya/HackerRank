-- Difficulty: medium
-- Problem: https://www.hackerrank.com/challenges/binary-search-tree-1/problem

SELECT N,
    CASE
        WHEN P IS NULL THEN "Root"
        WHEN N NOT IN (         -- when N not in [parent nodes]
            SELECT DISTINCT P
            FROM BST
            WHERE P IS NOT NULL
        ) THEN "Leaf"
        ELSE "Inner"
    END AS NodeType
FROM BST
ORDER BY N
