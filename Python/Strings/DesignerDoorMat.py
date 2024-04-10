# difficulty: easy
if __name__ == "__main__":
    welcome = "WELCOME"
    w_len = len(welcome)
    
    n, m = map(int, input().split())
    pattern = ".|."
    pattern_length = len(pattern)
    reverse = list()
    
    for i in range(1, (n+1)//2):
        pattern_no = 2*i - 1
        length = (m - pattern_length * pattern_no)//2
        string = "-" * length + pattern * pattern_no + "-"*length
        reverse.append(string)
        print(string)
    
    w_dash_length = (m - w_len)//2
    print("-" * w_dash_length + welcome + "-"*w_dash_length)
    reverse.reverse()
    for i in reverse:
        print(i)
