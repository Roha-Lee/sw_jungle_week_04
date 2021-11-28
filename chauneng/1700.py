from sys import stdin
import heapq

N, K = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))

nextSeq = [float('inf')]*(K+1)
newSeq = []
for i in range(K-1, -1, -1):
    num = seq[i]
    newSeq.append([-nextSeq[num], num])
    nextSeq[num] = i

gaget = [False]*(K+1)
plug = []
cnt = 0
while newSeq:
    n, g = newSeq.pop()

    if len(plug) < N:
        heapq.heappush(plug, [n, g])
        gaget[g] = True
    
    else:
        if gaget[g] is True:
            pass
        else:
            heapq.heappushpop(plug, [n, g])
            cnt += 1

print(cnt)