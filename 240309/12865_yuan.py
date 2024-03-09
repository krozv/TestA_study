# dp 문제임, 현재 배낭에서 최대가치를 더하거나 뺴기

def dfs(i,w,v):# 현재 넣는 물건인덱스, 이전 인덱스까지총물건무게, 이전인덱스까지 총가치
    global max_v

    if i == N:
        if w <= K:
            max_v = max(max_v,v)
        return

    # 물건 무게가 이미 무거우면 >k return
    if w > K:
        return
    # 남은 물건의 가치 다더해도 현재 max가치보다 작으면 return?
    if v + count_value[i] <= max_v:
        return
    else:
        dfs(i+1,w,v)
        dfs(i+1,w+lst[i][0],v+lst[i][1])

N, K = map(int,input().split())

#[w,v]
lst = [list(map(int,input().split())) for _ in range(N)]

# #i번쨰에 valuei+1번쨰~끝까지의 합 저장
# # value 1 2 3 / count-value = 2+3 3 0
count_value = [0]*(N)

for j in range(N-2,-1,-1):
    count_value[j] = count_value[j+1]+lst[j+1][1]

max_v = 0

dfs(0,0,0) # 현재 넣는 물건인덱스, 총물건무게, 총가치
print(max_v)

'''
n, k = map(int, input().split()))

item = [[0,0]]
dp = [[0] * (k+1) for _ in range(n+1)]

#[무게,가치] 형태로 item 에 추가 
for _ in range(n):
    item.append(list(map(int, input().split())))

#i는 개수 인덱스 j는 무게 인덱스
for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = item[i]
        if j >= w:
            dp[i][j] = max(dp[i-1][j] , dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[i][k])

'''

