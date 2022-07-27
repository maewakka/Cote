import sys
from collections import deque

def solution():
    N = sys.stdin.readline().strip()

    digit = "0123456789"
    count = [0 for i in range(len(digit))]
    set = 0

    for char in N:
        count[int(char)] += 1


    if (count[9]+count[6]) % 2 == 0:
        count[9] = (count[9] + count[6]) // 2
    else:
        count[9] = ((count[9] + count[6]) // 2) + 1
        
    count[6] = 0

    set = max(count)

    print(set)



if __name__ == "__main__":
    solution()