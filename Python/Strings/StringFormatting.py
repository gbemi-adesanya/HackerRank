# difficulty: easy
def convert(num, base):
    rem = -1
    converted_list = list()
    base_16 = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    
    while num > 0:
        rem = num % base
        num //= base
        a_check = rem
        if base == 16 and 9 < a_check < 16:
            rem = base_16.get(rem)
        converted_list.append(str(rem))
        
    converted_list.reverse()
    converted_num = "".join(converted_list)
    return converted_num

def print_formatted(number):
    # your code goes here
    max_binary = convert(number, 2)
    width = len(max_binary)
    for i in range(1, number+1):
        decimal = convert(i, 10)
        octal = convert(i, 8)
        hexa = convert(i, 16)
        binary = convert(i, 2)
        print("{:>{}} {:>{}} {:>{}} {:>{}}".format(decimal, width, octal, width, hexa, width, binary, width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)