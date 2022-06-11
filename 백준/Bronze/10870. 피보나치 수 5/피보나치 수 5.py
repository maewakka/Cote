import sys
sys.setrecursionlimit(10**6)
def main():
    N = int(sys.stdin.readline())

    def Fibonacci(N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        return Fibonacci(N-1) + Fibonacci(N-2)

    print(Fibonacci(N))

if __name__ == "__main__":
    main()