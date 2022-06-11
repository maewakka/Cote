import sys
sys.setrecursionlimit(10**6)
def main():
    N = int(sys.stdin.readline())

    def factorial(N):
        if N == 1 or N == 0:
            return 1
        else:
            return factorial(N-1) * N

    print(factorial(N))

if __name__ == "__main__":
    main()