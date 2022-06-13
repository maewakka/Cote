import sys

def main():
    N = int(sys.stdin.readline())

    min = N
    answer = 0

    for i in range(1,N):
        product = sum(list(map(int, list(str(i))))) + i
        if product == N and i <= min:
            min = i

    if min == N:
        answer = 0
    else:
        answer = min

    print(answer)

if __name__ == "__main__":
    main()