from collections import deque


# 교착 상태의 개수를 세는 함수 f 를 저으이
def f():

    # 교착 상태의 개수를 저장할 변수 cnt 를 정의
    cnt = 0
    for i in range(N):
        # 배열을 세로로 돌면서 0이 아닌 값이 있으면 q 에 wjwkd
        q = deque()
        for j in range(N):
            if table[j][i] != 0:
                q.append(table[j][i])

        # q 에 있는 값들을 꺼내서 2개씩 비교하며, 교착되는 지점이 있으면 cnt 를 1 추가
        p = deque()
        while q:
            p.append(q.popleft())

            if len(p) == 2:
                if p[0] == 1 and p[1] == 2:
                    cnt += 1
                p.popleft()

    return cnt


for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {f()}')

