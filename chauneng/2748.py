from sys import stdin

dp = [0, 1]

N = int(stdin.readline())

def fibonacci(n: int) -> int:
    
    n = 1
    tmp = int()

    while n <= N:
        n += 1
        tmp = dp[0] + dp[1]
        if n % 2:
            dp[0] = tmp
        else:
            dp[1] = tmp
    
    return tmp


if N >1:
    print(fibonacci(N))
else:
    print(N)