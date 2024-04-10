"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/find-a-string/problem
"""

def count_substring(string, sub_string):
    n = len(sub_string)
    count = 0
    for i in range(len(string)):
        if sub_string == string[i:i+n]:  # Slice the string according to the length of the substring
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
