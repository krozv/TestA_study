# 소프티어 산타의 텔레포트 (Lv.4)
# 산타 이동 = 1, 1 -> n, m / 이동 중 반드시 선물 Get
from collections import deque


# bfs 인자 : 시작점, 에너지 소모량 (e), 목표위치 (target)
def bfs(start_i, start_j, e, target):
    dq = deque([[start_i, start_j]])
    # 모든 영역 bfs
    while dq:
        # 닫힌 구역들 bfs
        portal = {}
        while dq:
            i, j = dq.popleft()
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                # 범위 내, 벽 x, 방문 x 면 동작
                if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] != -1 and v[ni][nj] == 0:
                    # 목표 위치 찾으면 종료 및 소모된 에너지 반환
                    if [ni, nj] == target:
                        return e
                    # 텔레포트 가능한 위치면 portal에 {수: [위치1, 위치2, ...]} 형태로 저장
                    elif arr[ni][nj] >= 10:
                        # 같은 수가 이미 저장돼 있다면
                        if portal.get(arr[ni][nj]):
                            portal[arr[ni][nj]].append([ni, nj])
                        else:
                            portal[arr[ni][nj]] = [[ni, nj]]
                    v[ni][nj] = e
                    dq.append([ni, nj])
        # 다른 닫힌 구역들로 이동
        e += 1
        # 현재 구역 내에서 찾았던 포탈들 순회
        for key, value in portal.items():
            # 순회한 포탈과 같은 종류의 (미리 찾아둔)모든 포탈 위치 순회
            for next_portal in teleport[key]:
                # 그 위치가 현재 구역 내의 포탈이 아니면 이동
                if next_portal not in value:
                    ni, nj = next_portal
                    if v[ni][nj] == 0:
                        v[ni][nj] = e
                        dq.append([ni, nj])

    return 0


n, m = map(int, input().split())

# -2=선물(단하나), -1=벽, 0=빈칸, 10~100,000=텔레포트
arr = [list(map(int, input().split())) for _ in range(n)]

# 순간이동 위치들 (teleport) 과 선물 위치 (target) 찾기
teleport = {}
for i in range(n):
    for j in range(m):
        if arr[i][j] >= 10:
            if not teleport.get(arr[i][j]):
                teleport[arr[i][j]] = []
            teleport[arr[i][j]].append([i, j])
        if arr[i][j] == -2:
            target = [i, j]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

# visited (v)
v = [[0] * m for _ in range(n)]
v[0][0] = 1

# 첫 번째 bfs : 시작 -> 선물
e1 = bfs(0, 0, 1, target)

# 선물 찾으면 배달하러 (현재까지 소모된 에너지 = e1 - 1)
# 선물 못 찾으면 print(-1)
if e1:

    # 시작점(i, j)을 선물 위치(target[0], target[1])로 갱신
    i, j = target[0], target[1]
    # 목표위치(target)를 배달 장소 (n-1, m-1)로 갱신
    target = [n-1, m-1]
    # visited (v) 초기화
    v = [[0] * m for _ in range(n)]
    v[i][j] = 1

    # 두 번째 bfs : 선물 -> 배달
    e2 = bfs(i, j, 1, target)
    # 배달 위치 찾으면 총 에너지 소모량 출력
    if e2:
        print(e1-1 + e2-1)
    # 배달 위치 못찾으면 -1
    else:
        print(-1)
else:
    print(-1)
