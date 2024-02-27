# 핀볼 게임

## dfs

recursion error 발생 -> try, except으로 처리
but, 47/50 시간초과 -> 시간 어떻게 줄이지?

```python
def f(x, y, s, dr):
    """
    x, y: 현재 위치 좌표
    s: 현재 획득한 score
    dr: 가고있는방향
    """
    global max_score
    try:
        delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        ni = x + delta[dr][0]
        nj = y + delta[dr][1]
        if 0<=ni<N and 0<=nj<N:
            # 처음 시작 위치인 경우 -> 종료
            if [ni, nj] == start:
                if max_score < s:
                    max_score = s
                return
            # 통로인 경우 -> 해당 방향 그대로 다음 탐색 시작
            if arr[ni][nj] == 0:
                f(ni, nj, s, dr)
            # 블록에 부딪힌 경우 -> score +1, 방향 전환 후 탐색 시작
            elif 1<=arr[ni][nj]<6:
                dr = block[arr[ni][nj]][dr]
                f(ni, nj, s+1, dr)
            # 웜홀인 경우 -> 해당 웜홀로 좌표 변환 후 탐색
            elif 6<=arr[ni][nj]<11:
                for w in wormhole[arr[ni][nj]]:
                    if w != [ni, nj]:
                        f(w[0], w[1], s, dr)
            # 블랙홀인 경우 -> return score
            elif arr[ni][nj] == -1:
                if max_score < s:
                    max_score = s
                return
        # 벽에 부딪힌 경우 -> score +1, 방향 전환 후 탐색
        else:
            f(ni, nj, s+1, (dr+2)%4)
    except:
        if max_score < s:
            max_score = s
        return
 
 
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 웜홀 위치 탐색
    wormhole = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] < 11:
                wormhole[arr[i][j]].append([i, j])
    # 블록 만났을 때 방향전환
    block = {1: [2, 3, 1, 0],
             2: [1, 3, 0, 2],
             3: [3, 2, 0, 1],
             4: [2, 0, 3, 1],
             5: [2, 3, 0, 1]}
    max_score = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for k in range(4):
                    start = [i, j]
                    f(i, j, 0, k)
    print(f'#{t} {max_score}')
```

## 반복문

반복문으로 변경 -> 호준이가 도와줌

```python
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 웜홀 위치 탐색
    wormhole = [[] for _ in range(11)]
    for i in range(N):
        for j in range(N):
            if 6 <= arr[i][j] < 11:
                wormhole[arr[i][j]].append([i, j])
    # 블록 만났을 때 방향전환
    block = {1: [2, 3, 1, 0],
             2: [1, 3, 0, 2],
             3: [3, 2, 0, 1],
             4: [2, 0, 3, 1],
             5: [2, 3, 0, 1]}
    max_score = 0
    # 0인 위치만 빼서 탐색하고
    # 함수말고 반복문으로
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                for k in range(4):
                    ni = i
                    nj = j
                    dr = k
                    s = 0
                    while True:
                        delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                        ni = ni + delta[dr][0]
                        nj = nj + delta[dr][1]
                        if 0 <= ni < N and 0 <= nj < N:
                            # 처음 시작 위치인 경우 -> 종료
                            if [ni, nj] == [i, j]:
                                if max_score < s:
                                    max_score = s
                                break
                            # 블록에 부딪힌 경우 -> score +1, 방향 전환 후 탐색 시작
                            if 1 <= arr[ni][nj] < 6:
                                dr = block[arr[ni][nj]][dr]
                                s += 1
                            # 웜홀인 경우 -> 해당 웜홀로 좌표 변환 후 탐색
                            elif 6 <= arr[ni][nj] < 11:
                                for w in wormhole[arr[ni][nj]]:
                                    # print(w)
                                    if w != [ni, nj]:
                                        ni = w[0]
                                        nj = w[1]
                                        break
                            # 블랙홀인 경우 -> return score
                            elif arr[ni][nj] == -1:
                                if max_score < s:
                                    max_score = s
                                break
                        # 벽에 부딪힌 경우 -> score +1, 방향 전환 후 탐색
                        else:
                            s += 1
                            dr = (dr + 2) % 4
    print(f'#{t} {max_score}')
```