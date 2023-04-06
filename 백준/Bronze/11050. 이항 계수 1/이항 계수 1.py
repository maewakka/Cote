import sys, math

def solution():
    n, k = map(int, sys.stdin.readline().split())

    print(math.factorial(n) // (math.factorial(k) * math.factorial(n-k)))

if __name__ == "__main__":
    solution()