from sys import stdin

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x: (-x[0], -x[1]))

lastEnd = float('inf')
ans = 0
for start, end in arr:
    if end <= lastEnd:
        ans += 1
        lastEnd = start
print(ans)