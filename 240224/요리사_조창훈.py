T = int(input())


def flavor_sum(food_list):
    # 맛의 조합은 두 가지 식재료에서만 나올 수 있다.
    # 모든 시너지를 합한 값이 맛이된다.
    result = 0
    for i in range(len(food_list) - 1):
        for j in range(i + 1, len(food_list)):
            # 첫 번째 선택한 식재료와, 두 번째 선택한 식재료의 시너지를 맛에 더한다.
            result += food_matrix[food_list[i]][food_list[j]]
            result += food_matrix[food_list[j]][food_list[i]]
    return result

def pick_foods(depth, idx):
    global min_flavor_diff
    B_food = []
    if depth == N // 2:
        # A음식의 식재료를 다 구함
        B_food = list(set(All_food)-set(A_food))
        A_flavor = flavor_sum(A_food)
        B_flavor = flavor_sum(B_food)
        tmp_diff = abs(A_flavor - B_flavor)
        if min_flavor_diff > tmp_diff:
            min_flavor_diff = tmp_diff
        return
    # 아직 다 구하기 전임
    for i in range(idx, N):
        A_food[depth] = All_food[i]
        pick_foods(depth+1,i+1)


for tc in range(1, T + 1):
    N = int(input())
    food_matrix = [list(map(int, input().split())) for _ in range(N)]
    # 푸드매트릭스에서 N//2개의 식재료를 골라 A음식의 재료로하고
    # 나머지 식재료를 골라 B음식의 식재료로 만든다.
    # 선택한 식재료를 표시할 배열
    picked_foods = [0] * N
    A_food = [0] * (N // 2)

    All_food = [i for i in range(N)]
    min_flavor_diff = 10 ** 8
    pick_foods(0,0)
    print(f'#{tc}',min_flavor_diff)
