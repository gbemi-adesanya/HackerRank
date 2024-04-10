"""
difficulty: easy
problem: https://www.hackerrank.com/challenges/nested-list/problem
"""

if __name__ == '__main__':
    records = list()
    scores = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        record = [name, score]
        records.append(record)
        scores.append(score)
        
    scores = sorted(set(scores))
    second_lowest = scores[1]
    output = [record[0] for record in records if record[1] == second_lowest]        
   
    output.sort()
    for i in output:
        print(i)
