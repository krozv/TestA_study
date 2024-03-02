'''
직원들의 키를 활용해 순열 생성 (순서가 상관 없으므로 부분집합의 개념 활용)
'''
def dfs(n,lst):
    global min_value
    if n >= N:
        if sum(lst) >= B:
            if min_value > sum(lst):
                min_value = sum(lst)
        return
    if visited[n] == 0:
        visited[n] = 1
        dfs(n+1, lst + [height[n]])
        dfs(n+1, lst)
        visited[n] = 0

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    # N은 점원의 수, B는 요구하는 최소 높이
    height = list(map(int,input().split()))
    min_value = 987654321
    visited = [0] * (N)
    dfs(0,[])
    print(f"#{tc} {min_value - B}")