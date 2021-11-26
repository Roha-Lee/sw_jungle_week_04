import sys 
def get_num_of_tiles(n):
    DP = [0, 1, 2]
    for i in range(3, n+1):
        DP[1], DP[2] = DP[2], (DP[1] + DP[2]) % 15746
    
    return DP[-1] if n > 2 else DP[n]


if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    print(get_num_of_tiles(n))