import sys

def main():
    N = int(sys.stdin.readline())

    digit = len(str(N))
    answer = N

    if digit > 2:
        for i in range(N-digit*9-1, N):
            product = sum(list(map(int, list(str(i))))) + i
            if product == N and i <= answer:
                answer = i
    else:  
        for i in range(0,N):
            product = sum(list(map(int, list(str(i))))) + i
            if product == N and i <= answer:
                answer = i

    if answer == N:
        answer = 0

    print(answer)

if __name__ == "__main__":
    main()