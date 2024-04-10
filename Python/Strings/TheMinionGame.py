# difficulty: medium
def minion_game(string):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    
    kevin, stuart = 0, 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin += length - i
        else:
            stuart += length - i
    if stuart > kevin:
        print("Stuart", stuart)
    elif stuart < kevin:
        print("Kevin", kevin)
    else:
        print("Draw")
      

if __name__ == '__main__':
    s = input()
    minion_game(s)
