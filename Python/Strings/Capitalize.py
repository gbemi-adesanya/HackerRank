# difficulty: easy
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(name):
    name_list = list(name)
    for i in range(len((name_list))):
        if i == 0 or name[i - 1] == " ":
            name_list[i] = name_list[i].upper()
    capitalized = "".join(name_list)
    return capitalized

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    fptr.write(result + '\n')
    fptr.close()
