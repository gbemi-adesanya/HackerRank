# difficulty: medium
def merge_the_tools(string, k):
    length = len(string)

    for i in range(0, length, k):
        t_string = string[i : i + k]
        # print(t_string)
        u_string = ""
        for j in t_string:
            if j not in u_string:
                u_string += j
        print(u_string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)