"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-the-captains-room/problem
"""

if __name__ == '__main__':
    group_size = int(input())
    room_list = list(map(int, input().split()))
    
    unique = set()
    groups = set()
    
    for i in room_list:
        if i in unique:
            groups.add(i)
        else:
            unique.add(i)
    
    captain = unique.difference(groups).pop()
    print(captain)
