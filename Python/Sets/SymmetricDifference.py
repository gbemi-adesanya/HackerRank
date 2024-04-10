"""
Difficulty: easy
Problem:
"""

if __name__ == "__main__":
    m = int(input())
    m_set = set(map(int, input().split()))
    
    n = int(input())
    n_set = set(map(int, input().split()))
    
    print_list = list()
    for i in m_set.difference(n_set):
        print_list.append(i)
    for i in n_set.difference(m_set):
        print_list.append(i)
        
    print_list.sort()
    for i in print_list:
        print(i)
