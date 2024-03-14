# 백준 15686 치킨 배달 (골드5)
def combination(i, cnt):
    global ans
    # 치킨집 m개 골랐으면
    if cnt == m:
        # 도시의 치킨 거리 구하기
        ss = 0
        for x in range(len(house)):
            hi, hj = house[x]
            # 각 집의 최소 치킨 거리 구하기
            min_distance = 100
            for y in range(len(chicken)):
                ci, cj = chicken[y]
                if bit[y]:
                    distance = abs(hi - ci) + abs(hj - cj)
                    if min_distance > distance:
                        min_distance = distance
            # 각 집의 최소 치킨 거리 합산 = 도시의 치킨 거리
            ss += min_distance
        # 도시의 최소 치킨 거리 찾기
        if ans > ss:
            ans = ss
        return
    # 모든 치킨집을 순회했으면 백
    if i == len(chicken):
        return
    # 조합 구현
    bit[i] = 1
    combination(i+1, cnt+1)
    bit[i] = 0
    combination(i+1, cnt)


# n (2~50), m (1~13)
n, m = map(int, input().split())
# 빈칸0, 집1 (1~2n), 치킨집2 (m~13)
arr = [list(map(int, input().split())) for _ in range(n)]

# 집과 치킨집의 좌표들을 각각 리스트화
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house.append([i, j])
        elif arr[i][j] == 2:
            chicken.append([i, j])

ans = 10**9

# 비트 리스트로 치킨집 m개 선택
bit = [0] * len(chicken)
combination(0, 0)

print(ans)
