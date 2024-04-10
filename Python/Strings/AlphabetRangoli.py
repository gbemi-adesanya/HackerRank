"""
Difficulty: easy
Problem: https://www.hackerrank.com/challenges/alphabet-rangoli/problem
"""

def mirror(input_list):
    # This function mirrors the list
    copy = input_list.copy()
    copy.pop()

    # Append everything in copy from the back to the front
    for i in range(len(copy)-1, -1, -1):
        # start: len(copy) - 1; the index of the last element in copy
        # stop: -1; the index before the first element (index 0) in copy
        # step: -1; move backwards (negative sign) by one step (1)
        input_list.append(copy[i])
    return input_list
    
def print_rangoli(size):
    lines = list()
    for i in range(size):
        lines.append([])

    # Populate arrays for mirroring
    for i in range(size-1, -1, -1):
        letter = chr(i+97)  # Change from unicode to character; a = 97
        for j in range(i+1):
            lines[j].append(letter)

    new_lines = list()
    for i in range(size):
        if len(lines[i]) != 1:
            mirror(lines[i])  # Mirror arrays to complete lines
        new_lines.append(lines[i)

    new_lines.reverse()  # Array is created in the wrong order, so .reverse()

    # Mirror array for printing
    width = 2 * size - 1
    new_list = mirror(new_lines)
    for i in range(len(new_list)):
        length = width - len(new_list[i])
        print("-" * length, end = "")
        print("-".join(new_list[i]), end="")
        print("-" * length)
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
