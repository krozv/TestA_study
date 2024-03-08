# 디저트 카페 swea 2105
def dfs(x, y):
    for d in range(2):
        next = [[x, y], [x, y]]
        lenth = [0, 0]
        while 0 <= next[d][0] < n and 0 <= next[d][1] < n:
            next[d][0] += dx[d]
            next[d][1] += dy[d]
            if v[arr[next[d][0]][next[d][1]]] == 0:
                v[arr[next[d][0]][next[d][1]]] = 1
                lenth[d] += 1
            else:
                break
        
        if lenth[d] == 0:
            return 0
            
            


T = int(input())
for case in range(1, T+1):
    # 한 변의 길이 (4 ~ 20)
    n = int(input())
    # 디저트 종류는 1 ~ 100
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx = (1, -1)
    dy = (1, 1)
    for i in range(n-2):
        for j in range(1, n-1):
            v = [0] * 101
            v[arr[i][j]] = 1
            temp = dfs(i, j) * 2

    print(f'#{case}', ans)

'''
좌우 대각 최대길이만큼 넓히고 (가다가 디저트 종류 겹치면 break)
다시 만나는 지점까지 좁히기
if 다 좁히면 cnt = sum(부모 대각선) * 2 - 4
    -> 다음 시작점으로 가서 처음부터 다시 동작
    (넓히는 길이가 최대 길이보다 작거나 같으면 pass)
else 못 좁히면 부모 대각선 최대 길이 1 감소
'''