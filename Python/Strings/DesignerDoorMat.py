"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/designer-door-mat/problem
"""

if __name__ == "__main__":
    n, m = map(int, input().split())
    pattern = ".|."
    pattern_length = len(pattern)
    array = list()

    for i in range(1, (n + 1) // 2):
        pattern_no = 2 * i - 1
        length = (m - pattern_length * pattern_no) // 2  # the number of dashes to be included with the pattern
        string = "-" * length + pattern * pattern_no + "-" * length
        array.append(string)
        print(string)

    word = "WELCOME"
    word_length = len(word)
    mid_length = (m - word_length) // 2  # the number of dashes to be included with WELCOME

    print("-" * mid_length + word + "-" * mid_length)
    array.reverse()
    for i in array:
        print(i)
