"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/re-split/problem
"""

regex_pattern = r"[,.]"

import re
print("\n".join(re.split(regex_pattern, input())))
