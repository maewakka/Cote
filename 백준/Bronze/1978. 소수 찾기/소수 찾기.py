import sys, math

def solution():
    n = int(sys.stdin.readline())
    inputs = list(map(int, sys.stdin.readline().split()))
    answer = 0

    m = max(inputs)
    primes = [True for i in range(m+1)]
    primes[0] = False
    primes[1] = False

    for i in range(2, round(math.sqrt(m)+1)):
        for j in range(i*2, m+1, i):
            primes[j] = False

    for input in inputs:
        if primes[input]:
            answer += 1

    print(answer)



if __name__ == "__main__":
    solution()