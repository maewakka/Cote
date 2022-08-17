import sys

def solution():
    N = int(sys.stdin.readline().strip())
    meetings = []
    answer = 0
    meeting = 0

    for i in range(N):
        meetings.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    meetings = sorted(meetings, key=lambda x:(x[1], x[0]))

    meeting = -1

    for i in range(N):
        if meetings[i][0] >= meeting:
            answer += 1
            meeting = meetings[i][1]

    print(answer)

if __name__ == "__main__":
    solution()