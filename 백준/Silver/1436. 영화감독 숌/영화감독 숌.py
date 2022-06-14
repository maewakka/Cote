import sys

def main():
    N = int(sys.stdin.readline())
    i = 666
    answer = 0

    while N != 0:
        temp = str(i)
        if "666" in temp:
            answer = i
            N-=1

        i+=1
    print(answer)

if __name__ == "__main__":
    main()