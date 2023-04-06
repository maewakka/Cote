import sys

def solution():
    answer = []
    while True:
        strings = sys.stdin.readline().rstrip()

        if strings == '.':
            break

        isBal = True
        stack = []
        open  = ['(', '[']
        close = [')', ']']

        for i in range(len(strings)):
            c = strings[i]
            if c in open:
                stack.append(c)
            if c in close:
                if stack and open[close.index(c)] == stack[-1]:
                    stack.pop()
                else:
                    isBal = False
                    break

        if stack:
            isBal = False

        if isBal:
            answer.append("yes")
        else:
            answer.append("no")


    for a in answer:
        print(a)

if __name__ == "__main__":
    solution()