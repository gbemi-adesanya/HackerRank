# difficulty: easy
if __name__ == '__main__':
    N = int(input())
    array = list()
    for i in range(N):
        instruction = list(input().split())
        # print(instruction)
        command = instruction[0]
        if command == "insert":
            pos, element = int(instruction[1]), int(instruction[2])
            array.insert(pos, element)
        elif command == "print":
            print("[", end = "")
            for i in range(len(array)):
                if i < len(array) - 1:
                    print(str(array[i]) + ", ", end = "")
                else:
                    print(array[i], end = "")
            print("]")
        elif command == "remove":
            element = int(instruction[1])
            array.remove(element)
        elif command == "append":
            element = int(instruction[1])
            array.append(element)
        elif command == "sort":
            array.sort()
        elif command == "pop":
            array.pop()
        elif command == "reverse":
            array.reverse()
