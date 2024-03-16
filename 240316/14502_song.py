# 14502_연구소
'''
https://www.acmicpc.net/problem/14502
풀이 보고 풀었음
bfs + dfs(조합) 문제
itertools 사용했는데 백트래킹으로 조합 구하는 방식도 시도하기
'''
import copy
from collections import deque
from itertools import combinations

def wall(c):
    for c in combinations(x_y, 3):
        for i in c:
            virus[i[1]][i[0]] = 1
        spread()
        for i in c:
            virus[i[1]][i[0]] = 0

def spread():
    virus2 = copy.deepcopy(virus)

    point = deque(start)
    while point:
        x, y = point.popleft()
        for d in [1, 0], [-1, 0], [0, 1], [0, -1]:
            mx = x + d[0]
            my = y + d[1]
            if 0 <= mx < m and 0 <= my < n and virus2[my][mx] == 0:
                point.append([mx, my])
                virus2[my][mx] = 2

    global result
    cnt = 0
    for v in virus2:
        cnt += v.count(0)
    if result < cnt:
        result = cnt

n, m = map(int, input().split())

virus = []
start = []
result = 0

for y in range(n):
    virus.append(list(map(int, input().split())))
    for x in range(m):
        if virus[y][x] == 2:
            start.append([x, y])

x_y = [(x, y) for x in range(m) for y in range(n) if not virus[y][x]]

wall(0)
print(result)