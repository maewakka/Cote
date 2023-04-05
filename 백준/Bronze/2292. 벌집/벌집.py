import sys

def solution():
    n = int(sys.stdin.readline())

    index = 1
    count = 6
    depth = 2

    if n == 1:
        print(1)
        return

    while count < n+count:
        start, end = index+1, index + count

        if n >= start and n <= end:
            print(depth)
            break

        depth += 1
        index += count
        count += 6


if __name__ == "__main__":
    solution()