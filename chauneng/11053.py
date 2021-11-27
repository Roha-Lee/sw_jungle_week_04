from sys import stdin

N = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

dp = [1]*N

for j in range(1, N):
    for i in range(j):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i]+1)

print(max(dp))