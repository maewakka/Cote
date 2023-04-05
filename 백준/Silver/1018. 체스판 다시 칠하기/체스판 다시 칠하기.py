import sys

def change_count(Board):
    w_count = 0
    b_count = 0

    W_Board = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
    B_Board = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']

    for x in range(8):
        for y in range(8):
            if Board[x][y] != W_Board[x][y]:
                w_count += 1
            if Board[x][y] != B_Board[x][y]:
                b_count += 1

    return min(w_count, b_count)

def slice_board(Board, x, y):
    board = []

    for i in range(x, x+8):
        board.append(Board[i][y:y+8])

    return board

def solution():
    n, m = map(int, sys.stdin.readline().split())

    Board = []
    answer = sys.maxsize

    for i in range(n):
        Board.append(sys.stdin.readline().strip())

    for x in range(n+1-8):
        for y in range(m+1-8):
            answer = min(answer, change_count(slice_board(Board, x, y)))

    print(answer)

if __name__ == "__main__":
    solution()