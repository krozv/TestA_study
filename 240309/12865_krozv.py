# 12865. 평범한 배낭
"""
N개의 물건
무게 W, 가치 V, 최대무게 K
"""
def perm(i, s, v):
    """
    i: 현재 weight 번호
    s: 총 무게 합
    v: 총 가치 합
    """
    global max_v
    
    if s >= K:
        if s > K:
            v -= info[i][1]
        if max_v < v:
            max_v = v
        return

    if i == N-1:
        if max_v < v:
            max_v = v
        return


    for j in range(i, N):
        if visited[j] == 0:
            visited[j] = 1
            perm(j, s+info[j][0], v+info[j][1])
            visited[j] = 0


import sys
sys.stdin = open('input.txt', 'r')
N, K = map(int, input().split())    # 1<=N<=100, 1<=K<=100,000
info = []
for _ in range(N):
    W, V = map(int, input().split())    # 1<=W<=100,000, 0<=V<=1,000
    info.append([W, V])
visited = [0] * N
max_v = 0
perm(0, 0, 0)
print(max_v)