from sys import stdin
import heapq

N = int(stdin.readline())

arr = []
for _ in range(N):
    start, end = map(int, stdin.readline().split())
    heapq.heappush(arr, ((end-start), start))

ans = 0
timeline = [False]*(2**31)

while arr:
    length, start = heapq.heappop(arr)
    flag = True
    for i in range(length):
        if timeline[start+i] is True:
            flag = False
            break
    if flag:
        ans += 1
        for i in range(length):
            timeline[start+i] = True

print(ans)