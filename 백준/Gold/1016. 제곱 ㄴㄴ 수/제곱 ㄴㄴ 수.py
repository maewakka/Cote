import sys
import math

def solution():
    A, B = map(int, sys.stdin.readline().strip().split(' '))
    numbers = []
    sqrt = 2
    answer = 0

    for i in range(A, B+1):
        numbers.append(i)

    while sqrt ** 2 <= B:
        number = sqrt ** 2
        if A % number != 0:
            first_index = (number * ((A // number) + 1)) - A
        else:
            first_index = (number * ((A // number))) - A
        for i in range(first_index, len(numbers), number):
            numbers[i] = 0

        sqrt += 1

    for number in numbers:
        if number != 0:
            answer += 1

    print(answer)

if __name__ == "__main__":
    solution()