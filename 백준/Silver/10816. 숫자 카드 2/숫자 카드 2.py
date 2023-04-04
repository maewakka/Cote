import sys

def solution():
    n = int(sys.stdin.readline())

    cards = {}
    inputs = list(map(int, sys.stdin.readline().split()))

    for input in inputs:
        if cards.get(input) == None:
            cards[input] = 0
        cards[input] += 1

    m = int(sys.stdin.readline())
    answer = []

    inputs = list(map(int, sys.stdin.readline().split()))
    for input in inputs:
        if cards.get(input) == None:
            answer.append('0')
        else:
            answer.append(str(cards[input]))

    print(' '.join(answer))

if __name__ == "__main__":
    solution()