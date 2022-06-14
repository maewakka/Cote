import sys

def main():
    N = int(sys.stdin.readline())
    num_list = []

    for i in range(N):
        num_list.append(int(sys.stdin.readline()))

    for i in range(N):
        max = -1001
        index = -1
        for j in range(N-i):
            if num_list[j] >= max:
                max = num_list[j]
                index = j

        temp = num_list[index]
        num_list[index] = num_list[N-i-1]
        num_list[N-i-1] = temp

    for i in num_list:
        print(i)

if __name__ == "__main__":
    main()