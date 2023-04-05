import sys

def solution():
    n = int(sys.stdin.readline().strip())
    num = 666
    count = 0

    while True:
        if str(num).find("666") >= 0:
            count += 1

        if count == n:
            break

        num += 1

    print(num)

if __name__ == "__main__":
    solution()