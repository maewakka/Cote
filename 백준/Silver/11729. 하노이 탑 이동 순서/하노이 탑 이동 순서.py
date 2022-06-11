import sys
sys.setrecursionlimit(10**6)
def main():
    N = int(sys.stdin.readline())

    print((2**N) - 1)

    def hanoi(N, start_point, destination_point, sub_point):
        if N == 1:
            print(start_point, destination_point)
            return 0

        hanoi(N-1, start_point, sub_point, destination_point)
        print(start_point, destination_point)
        hanoi(N-1, sub_point, destination_point, start_point)

    hanoi(N, 1, 3, 2)

if __name__ == "__main__":
    main()