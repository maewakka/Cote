import sys
sys.setrecursionlimit(10**6)

if __name__ == "__main__":

    n = int(sys.stdin.readline().strip())
    n_tile = [0 for i in range(n+1)]
    
    def tile(x):
        if x == 1:
            return 1
        if x == 2:
            return 2
    
        if n_tile[x] == 0:
            n_tile[x] = tile(x-1) + tile(x-2)
           
        return n_tile[x]
    
    print(tile(n) % 10007)