# 1
# 5 16
# 1 3 3 5 6
def dfs(depth, s, start):
    global min_diff
    if s >= B:
        if min_diff > s-B:
            min_diff = s-B
        return
    if depth == N:
        return
    for i in range(start, N):
        need_member.append(member_list[i])
        dfs(depth + 1, s + member_list[i], i + 1)
        need_member.pop()

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    member_list = list(map(int, input().split()))
    need_member = []
    min_diff = 20000
    dfs(0,0,0)
    print(f'{tc} {min_diff}')
