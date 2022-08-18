import sys
import math

def solution():
    M, N = map(int, sys.stdin.readline().strip().split(' '))
    numbers = []
    answer = []

    for i in range(N+1):
        numbers.append(i)

    sqrt = int(math.sqrt(N))

    for i in range(2, sqrt + 1):
        for j in range(i*2, N+1, i):
            numbers[j] = 0


    for number in numbers:
        if number != 0 and number != 1 and number >= M:
            answer.append(number)

    for number in answer:
        print(number)

if __name__ == "__main__":
    solution()