import sys
from queue import PriorityQueue

def solution():
    N = int(sys.stdin.readline().strip())
    cards = PriorityQueue()
    answer = 0

    for i in range(N):
        cards.put(int(sys.stdin.readline().strip()))

    while cards.qsize() > 1:
        data1 = cards.get()
        data2 = cards.get()
        sum = data1 + data2
        cards.put(sum)
        answer += sum
        
    print(answer)

if __name__ == "__main__":
    solution()