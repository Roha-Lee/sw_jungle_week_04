from sys import stdin

N = int(stdin.readline())

dp = [[float('inf')]*(N+1) for _ in range(N+1)]
arr = [0]
for i in range(N):
    a, b = map(int, stdin.readline().split())
    dp[i+1][i+1] = a, b, 0

for i in range(1, N):
    for j in range(1, N):
        if i<j:
            dp[i][j] = dp[i][i][0], dp[j][j][1], min(dp[i][j], dp[i][i][0] * dp[i][i][1] * dp[j][j][1] + (dp[i][i][2] + dp[j][j][2]))
            print(dp[i][j][2])


print(dp)
