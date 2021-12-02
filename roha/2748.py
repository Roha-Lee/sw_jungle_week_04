import sys 
def fibo(n):
    DP = [0] * (n+1)
    DP[1] = 1
    for i in range(2, n+1):
        DP[i] = DP[i-1] + DP[i-2]
    return DP[n]
if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())   
    print(fibo(n))