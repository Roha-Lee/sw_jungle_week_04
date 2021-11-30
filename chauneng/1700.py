from sys import stdin

N, K = map(int, stdin.readline().split())
seq = list(map(int, stdin.readline().split()))

nextTurn = [float('inf')]*(K+1)
newSeq = []
for i in range(K-1, -1, -1):
    num = seq[i]
    newSeq.append([nextTurn[num], num])
    nextTurn[num] = i

using = [0]*(K+1)
plug = set()
cnt = 0
while newSeq:
    nextUse, gaget = newSeq.pop()
    
    if gaget in plug:
        using[gaget] = nextUse
        continue

    plug.add(gaget)
    if len(plug)<=N:
        using[gaget] = nextUse
        continue
    plug = plug - {using.index(max(using))}
    using[using.index(max(using))] = 0

    using[gaget] = nextUse
    cnt += 1

print(cnt)