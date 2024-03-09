# 12865.평범한 배낭
### 첫시도
6%에서 시간초과
```python
def f(i, weight,value):
    global max_val
    if max_val < value:
        max_val = value

    for j in range(i, N):
        if weight+WV[j][0] <= K:
            f(j+1, weight+WV[j][0], value+WV[j][1])

import sys
input = sys.stdin.readline
N, K = map(int,input().split())
WV = [list(map(int,input().split())) for _ in range(N)]#[무게,가치]
max_val = 0
f(0,0,0)
print(max_val)
```

