# 요리사
"""
N개의 식재료
식재료를 N/2개씩 나누어 두 개의 요리 (N 짝수)
A음식, B음식
맛의 차이가 최소가 되도록 재료 배분
백트래킹 or 수열
"""
def f(i, n):
    if i == N:
        return
    # 1개수 세기
    if n == N//2:
        A = 0
        B = 0
        # print(visit)
        for i in range(N):
            for j in range(N):
                if visit[i] == 1 and visit[j] == 1:
                    A += arr[i][j]
                if visit[i] == 0 and visit[j] == 0:
                    B += arr[i][j]
        global min_v
        if min_v > abs(A-B):
            min_v = abs(A - B)
        return
    # 1개수 불충분 시 1추가
    else:
        visit[i] = 1
        f(i+1, n+1)
        visit[i] = 0
        f(i+1, n)


import sys
sys.stdin = open('sample_input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    min_v = 100000
    f(0, 0)
    print(f'#{t} {min_v}')

