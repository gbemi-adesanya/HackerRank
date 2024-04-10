# difficulty: easy
def mutate_string(string, position, character):
    array = list(string)
    array[position] = character
    string = "".join(array)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
