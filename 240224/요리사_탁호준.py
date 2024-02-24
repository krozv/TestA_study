# 재료에 대한 시너지 차이를 구하는 함수
def synergy_gap(data_A, data_B):  # data1: A음식에 들어갈 재료 리스트, data2: B음식에 들어갈 재료 리스트
    taste_A, taste_B = 0, 0  # 재료들의 시너지로 인한 A와 B의 맛
    while data_A:  # 재료가 더 이상 없을 때 까지
        food1 = data_A.pop()  # 음식 꺼내기
        for food2 in data_A:  # 남은 재료들을 순회
            taste_A += synergy[food1][food2] + synergy[food2][food1]  # 시너지 더해주기
    while data_B:
        food1 = data_B.pop()
        for food2 in data_B:
            taste_B += synergy[food1][food2] + synergy[food2][food1]
    return abs(taste_B - taste_A)  # 맛차이 반환

# 재료 선정을 위한 함수
def select_ingredient(i:int, A:list, B:list):  # i:추가해야 할 재료, A,B:재료 리스트
    global min_taste_gap
    if len(A) == N // 2:  # A음식에 필요한 재료가 다 골라진 경우
        taste_gap = synergy_gap(A, B + list(range(i, N))) #B에 i부터 N-1번 재료까지 다 넣기
        if min_taste_gap > taste_gap:
            min_taste_gap = taste_gap
    elif len(B) == N // 2:
        taste_gap = synergy_gap(A+list(range(i, N)), B) #A에 i부터 N-1번 재료까지 다 넣기
        if min_taste_gap > taste_gap:
            min_taste_gap = taste_gap
    else:
        select_ingredient(i+1, A+[i], B)
        select_ingredient(i+1, A, B+[i])
    return

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    l1 = []  # A음식에 들어갈 리스트
    l2 = []  # B음식에 들어갈 리스트
    min_taste_gap = 20000 * N ** 2
    select_ingredient(0, l1, l2)
    print(f'#{tc} {min_taste_gap}')