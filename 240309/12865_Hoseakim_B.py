# 백준 12865 평범한 배낭
# https://www.acmicpc.net/problem/12865

# n(1 ~ 100)개의 물건, 무게 제한 k(1 ~ 100,000)
n, k = map(int, input().split())
# 무게 w(1 ~ 100,000), 가치 v(1 ~ 1,000)
info = [list(map(int, input().split())) for _ in range(n)]

# 물품의 수가 최대 100개
# 즉, 최대 경우의 수 = 2^100 (시간 복잡도 2^n)
# (= 1,267,650,600,228,229,401,496,703,205,376)
# 따라서, 조합을 따질 거라면 무조건 백트래킹이 필요

# info.sort(key=lambda x: x[1], reverse=True)
# info.sort(key=lambda x: x[0], reverse=True)
remain_v = 0
remain_w = 0
for i in range(n):
    remain_v += info[i][1]
    remain_w += info[i][0]

def combination(i):
    global max_v
    global remain_v
    global remain_w
    global w
    global v
    if v + remain_v <= max_v:
        return
    if w + remain_w <= k:
        v += remain_v
        if max_v < v:
            max_v = v
        v -= remain_v
        return
    if w >= k or i == n:
        if max_v < v:
            max_v = v
        return
    else:
        remain_v -= info[i][1]
        remain_w -= info[i][0]
        if w+info[i][0] <= k:
            w += info[i][0]
            v += info[i][1]
            combination(i+1)
            w -= info[i][0]
            v -= info[i][1]
        combination(i+1)
        remain_v += info[i][1]
        remain_w += info[i][0]

max_v = 0
w = 0
v = 0
combination(0)

print(max_v)