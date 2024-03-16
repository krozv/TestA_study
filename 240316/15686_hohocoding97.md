# 15686. 치킨 배달
### 코드
pypy3-148ms
```python
import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())

city = [list(map(int,input().split())) for _ in range(N)]
chiken = []
house_pos = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chiken.append((i,j))
        elif city[i][j] == 1:
            house_pos.append((i,j))
C = len(chiken)
H = len(house_pos)

result = 2*N*H
data = combinations(chiken, M) #M개 치킨 집 조합
for datum in data:
    min_sum = 0
    for pos in house_pos:
        min_d = 2*N
        for r,c in datum: #치킨집 위치
            d = abs(pos[0]-r) + abs(pos[1]-c)
            if min_d > d:
                min_d = d
        min_sum += min_d
    if result > min_sum:
        result = min_sum
print(result)
```