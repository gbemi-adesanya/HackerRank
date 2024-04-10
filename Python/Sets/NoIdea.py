"""
Difficulty: medium
Problem:
"""

if __name__ == "__main__":
    first = input()
    n, m = first.split()
    
    array = list(map(int, input().split()))
    
    a_set = set(map(int, input().split()))
    b_set = set(map(int, input().split()))
    
    happiness = 0
    for i in array:
        if i in a_set:
            happiness += 1
        if i in b_set:
            happiness -= 1
            
    print(happiness)
