# 수영장
"""
완전탐색
경우의 수

깔끔하게 바꾸려면
1. 3달권 결제 -> 그냥 12개월 넘어가면 return 할 수 있도록
2. 1달권 결제와 1일권 결제를 합쳐서 다음 단계로 가도록
"""

def f(i, m1, m3, d1):
    global min_val
    # 12월까지 다 계산
    if i == 12:
        c = m1*M1 + m3*M3 + d1*D1
        if min_val > c:
            min_val = c
        return
    # 아직 계산 안함
    if arr[i]:
        # 3달권 결제
        if i < 10:
            for j in range(i, i+3):
                visit[j] = 1
            f(i+3, m1, m3+1, d1)
            for j in range(i, i + 3):
                visit[j] = 0
        else:
            for j in range(i, 12):
                visit[j] = 1
            f(i+(12-i), m1, m3 + 1, d1)
            for j in range(i, 12):
                visit[j] = 0
        # 1달권 결제
        visit[i] = 1
        f(i+1, m1+1, m3, d1)
        visit[i] = 0
        # 1달을 1일권으로 결제
        visit[i] = 1
        d2 = d1 + arr[i]
        f(i+1, m1, m3, d2)
        visit[i] = 0
    else:
        f(i+1, m1, m3, d1)

import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    D1, M1, M3, Y1 = map(int, input().split())
    arr = list(map(int, input().split()))
    visit = [0] * 12
    min_val = Y1
    f(0, 0, 0, 0)
    print(f'#{t} {min_val}')