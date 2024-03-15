# 14500. 테트로미노

### 코드
440ms
```python
import sys
input = sys.stdin.readline

#테트리미노 모양만들기(ㅗ모양 제외)
def make_t(k, positions):
    global max_max_sum
    if k == 4:
        result = find_max(positions)
        if max_max_sum < result:
            max_max_sum = result
        return
    else:
        i, j = positions[-1]
        for ni, nj in [(i,j+1),(i+1,j),(i-1,j),(i,j-1)]:
            if (ni,nj) not in positions:
                make_t(k+1, positions+[(ni,nj)])

#ㅗ모양(이거 예외가 있는걸 모르고 있었음..)
def make_h():
    global max_max_sum
    for i in range(1,5):
        A = [(0,0),(0,1),(1,0),(-1,0),(0,-1)]
        A.pop(i)
        result = find_max(A)
        if max_max_sum < result:
            max_max_sum = result

def find_max(positions):
    max_sum = 0
    for r in range(N):
        for c in range(M):
            sum = 0
            for dr,dc in positions:
                nr, nc = r+dr, c+dc
                if 0<=nr<N and 0<=nc<M:
                    sum += data[nr][nc]
            if max_sum < sum:
                max_sum = sum
    return max_sum


N, M = map(int,input().split()) #세로, 가로
data = [list(map(int, input().split())) for _ in range(N)]
max_max_sum = 0
make_t(1,[(0,0)])   #테트로미노(ㅗ모양제외) 확인
make_h()            #ㅗ모양에 대해서만 확인
print(max_max_sum)
```