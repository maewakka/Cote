import sys
import re

def solution():
    line = sys.stdin.readline().strip()
    number = []
    answer = []
    temp = 0

    for i in range(len(line)):
        this_char = line[i]

        if this_char == '+':
            temp += int(''.join(number))
            number = []
        elif this_char == '-':
            temp += int(''.join(number))
            answer.append(temp)
            temp = 0
            number = []
        else:
            number.append(this_char)

        if i == len(line)-1:
            temp += int(''.join(number))
            answer.append(temp)


    result = answer[0]

    if len(answer) > 1:
        for i in range(1, len(answer)):
            result -= answer[i]

    print(result)

if __name__ == "__main__":
    solution()