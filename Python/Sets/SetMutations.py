"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem
"""

if __name__ == '__main__':
    num_A = int(input())
    A_set = set(map(int, input().split()))
    num_other = int(input())

    set_list = list()
    func_list = list()
    for i in range(num_other):
        function_name, num_elements = input().split()
        func_list.append(function_name)
        other_set = set(map(int, input().split()))
        set_list.append(other_set)       
    
    for i in range(num_other):
        first_letter = func_list[i][0]
        if first_letter == "i":
            A_set.intersection_update(set_list[i])
        elif first_letter == "u":
            A_set.update(set_list[i])
        elif first_letter == "s":
            A_set.symmetric_difference_update(set_list[i])
        elif first_letter == "d":
            A_set.difference_update(set_list[i])
    
    print(sum(A_set))
