"""
높이가 B인 선반
N명의 선반
탑의 높이 B
brute force or greedy?
"""
def f(a, b, s, n):
    """
    a: 점원 명 수
    b: 마지막 방문한 인덱스
    s: 현재까지 합
    n: 현재까지 명 수
    """
    global sub
    if s - B == 0:
        sub = 0
        return
    if a == n:
        if 0 < s - B < sub:
            sub = s - B
        return
    for i in range(b, N):
        if not visited[i]:
            visited[i] = 1
            f(a, i, s+arr[i], n+1)
            visited[i] = 0


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0] * N
    sub = max(arr)
    for i in range(N+1):
        f(i, 0, 0, 0)
    print(f'#{t} {sub}')