import sys
from collections import deque


def solution():
    n = int(sys.stdin.readline())

    deck = deque([i for i in range(1, n+1)])

    while len(deck) > 1:
        deck.popleft()
        deck.append(deck.popleft())


    print(deck[0])

if __name__ == "__main__":
    solution()
