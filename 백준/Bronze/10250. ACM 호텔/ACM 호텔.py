import sys

def solution():
    case = int(sys.stdin.readline())
    answer = []

    for _ in range(case):
        h, w, n = map(int, sys.stdin.readline().split())


        floor = n % h
        if floor == 0:
            floor = str(h)
        else:
            floor = str(floor)
        num = ((n-1) // h) + 1
        if num < 10:
            num = '0' + str(num)
        else:
            num = str(num)


        answer.append(floor + num)

    for a in answer:
        print(int(a))

if __name__ == "__main__":
    solution()