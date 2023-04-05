import sys, math

def solution():
    a, b = map(int, sys.stdin.readline().split())
    gcd = math.gcd(a, b)
    print(gcd)
    print(a * b // gcd)

if __name__ == "__main__":
    solution()