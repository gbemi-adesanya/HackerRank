# difficulty: easy
def mirror(input_list):
    center = input_list[len(input_list) - 1]
    new = list()
    for i in input_list:
        # print(i)
        if i != center:
            # print(i)
            new.append(i)
        else:
            break

    for i in range(len((new))-1, -1, -1):
        input_list.append(new[i])

    return input_list
    
def print_rangoli(size):
    dashes = 2*size - 1
    lines = list()
    for i in range(size):
        lines.append([])

    for i in range(size-1, -1, -1):
        letter = chr(i+97)
        for j in range(i+1):
            lines[j].append(letter)

    new_lines = list()
    for i in range(size):
        if len(lines[i]) == 1:
            new = lines[i]
        else:
            new = mirror(lines[i])
        new_lines.append(new)

    new_lines.reverse()

    new_list = mirror(new_lines)
    string_list = list()
    for i in range(len(new_list)):
        c = ""
        length = dashes - len(new_list[i])
        c += "-" * length
        c += "-".join(new_list[i])
        c += "-" * length
        string_list.append(c)
        print("-" * length, end = "")
        print("-".join(new_list[i]), end="")
        print("-" * length)

    string = "\n".join(string_list)
    return string

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
