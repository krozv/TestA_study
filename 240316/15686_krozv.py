"""
도시의 치킨거리 가장 작게
combination + dfs
M<=치킨집<=13
치킨집을 M개만 고름 -> 치킨 거리의 최솟값
"""
import sys
from itertools import combinations
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
home_lst = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home_lst.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])

existed_chicken = list(combinations(chicken, M))

min_total = 2*N*len(home_lst)

for existed in existed_chicken:
    total_d = 0
    for home in home_lst:
        r1, c1 = home
        min_d = 2*N
        for store in existed:
            r2, c2 = store
            d = abs(r1-r2) + abs(c1-c2)
            min_d = min(min_d, d)
        total_d += min_d
        if total_d > min_total:
            break

    min_total = min(min_total, total_d)
print(min_total)