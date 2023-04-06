import sys

def solution():
    a, b, v = map(int, sys.stdin.readline().split())

    day = (v-a) // (a-b)
    if day == 0 and v >= a-b:
        day = 1
    height = v - (day * (a-b))

    if a >= v:
        print(1)
        return

    while True:
        day += 1

        height -= a
        if height <= 0:
            break

        height += b

    print(day)

if __name__ == "__main__":
    solution()