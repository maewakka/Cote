import sys

def main():
    M, N = map(int, sys.stdin.readline().split())
    board = []
    white_board = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']
    black_board = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
    min_change = 64

    for i in range(M):
        board.append(sys.stdin.readline().strip())

    def check_board(list):
        W_Check = 0
        B_Check = 0
        for i in range(8):
            for j in range(8):
                if list[i][j] != white_board[i][j]:
                    W_Check += 1
                if list[i][j] != black_board[i][j]:
                    B_Check += 1

        if W_Check >= B_Check:
            return B_Check
        else:
            return W_Check


    for i in range(M-7):
        for j in range(N-7):
            slice_board = []
            for k in range(8):
                slice_board.append(board[i+k][j:j+8])
            result = check_board(slice_board)
            if result <= min_change:
                min_change = result

    print(min_change)

if __name__ == "__main__":
    main()