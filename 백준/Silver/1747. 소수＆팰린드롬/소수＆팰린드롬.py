import sys
import math

def solution():
    N = int(sys.stdin.readline().strip())
    numbers = []
    primes = []
    answer = 0

    for i in range(1004000):
        numbers.append(i)

    for i in range(2, int(math.sqrt(1004000)) + 1):
        for j in range(i*2, len(numbers), i):
            numbers[j] = 0

    for number in numbers:
        if number != 0 and number != 1:
            primes.append(number)

    for i in range(len(primes)):
        if primes[i] >= N:
            tempString = str(primes[i])
            if tempString[::-1] == tempString:
                answer = primes[i]
                break

    print(answer)


if __name__ == "__main__":
    solution()