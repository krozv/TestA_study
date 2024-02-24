# 프로세서 연결하기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
sys.stdout = open('output.txt', 'w')

def wiring(i, ss, cnt):
    global max_connection
    global min_len
    if i == len(core_list):
        if max_connection < cnt:
            max_connection = cnt
            min_len = ss
            return
        elif max_connection == cnt and min_len > ss:
            min_len = ss
            return
        return

    if (
        core_list[i][0] == 0 or core_list[i][0] == n-1 or
        core_list[i][1] == 0 or core_list[i][1] == n-1
    ):
        wiring(i+1, ss, cnt+1)
        return

    for d in range(4):
        w_len = 0
        flag = 0
        connection = 0
        for k in range(1, n):
            ni = core_list[i][0] + dx[d] * k
            nj = core_list[i][1] + dy[d] * k
            if 0 <= ni < n and 0 <= nj < n:
                if arr[ni][nj] > 0:
                    for j in range(1, w_len+1):
                        ni = core_list[i][0] + dx[d] * j
                        nj = core_list[i][1] + dy[d] * j
                        arr[ni][nj] = 0
                    w_len = 0
                    if d == 3:
                        if i+1 == len(core_list):
                            flag = 0
                        else:
                            flag = 1
                    break
                else:
                    w_len += 1
                    arr[ni][nj] = 2
                    if ni == 0 or ni == n - 1 or nj == 0 or nj == n - 1:
                        connection = 1
                        flag = 1
                        break
        if flag == 1:
            wiring(i+1, ss+w_len, cnt+connection)
            for j in range(1, w_len+1):
                ni = core_list[i][0] + dx[d] * j
                nj = core_list[i][1] + dy[d] * j
                arr[ni][nj] = 0


def find_core():
    result = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                result.append([i, j])
    return result


T = int(input())
for case in range(1, T+1):
    n = int(input())    # 셀 크기 = n * n
    # 0: 빈 셀, 1: 코어
    arr = [list(map(int, input().split())) for _ in range(n)]

    core_list = find_core()

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    min_len = 10**9
    max_connection = 0

    wiring(0, 0, 0)

    print(f'#{case}', min_len)
