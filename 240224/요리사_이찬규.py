'''
두 명의 손님에게 음식 제공, 식성이 비슷한 2명이기에 최대한 비슷한 맛의 음식
N개의 식재료
식재료를 각각 N/2개씩 나누어 2개의 요리 (N은 짝수)
각각 만들어진 2개의 A음식과 B음식의 맛 차이가 최소가 되도록 재료를 배분

테스트 케이스 수 T
식재료의 수 N
N개의 줄에 N*N의 시너지

1. 시간 제한 : 최대 50개 테스트 케이스를 모두 통과하는 데 C / C++ / Java 모두 3초
2. 식재료의 수 N은 4이상 16이하의 짝수이다. (4 ≤ N ≤ 16)
3. 시너지 Sij는 1이상 20,000이하의 정수이다. (1 ≤ Sij ≤ 20,000, i ≠ j)
4. i와 j가 서로 같은 경우의 Sij값은 정의되지 않는다. 입력에서는 0으로 주어진다.
'''


from collections import deque
from itertools import combinations


# 두 음식 간의 시너지의 차이를 구해줄 함수 yes_chef
def yes_chef():
    # 식재료의 절반으로 만들 수 있는 조합을 만들어줌
    ii = list(combinations(i, N//2))
    m = 0
    n = len(ii)

    # 이 때, 조합이 순서대로 만들어지므로 맨 앞과 맨 뒤, 앞에서 2번째와 뒤에서 2번째 ... 이런 식으로 2쌍씩이 재료를 둘로 나눈 경우의 수임을 알 수 있다.
    # 종료 조건은 절반까지 순회했을 때
    while m < n//2:
        # 따라서 두 개의 식재료로 나눠주고
        c1 = ii[0+m]
        c2 = ii[-(1+m)]

        # 두 재료 간의 시너지를 더해줄 c1s, c2s 를 정의
        c1s = 0
        c2s = 0

        # 전체를 순회하며 시너지를 더해줌. 두 재료가 같은 경우는 0이므로 영향을 주지 않는다.
        for j in range(N//2-1):
            for k in range(j+1, N//2):
                c1s += S[c1[j]][c1[k]] + S[c1[k]][c1[j]]
                c2s += S[c2[j]][c2[k]] + S[c2[k]][c2[j]]

        # 두 시너지의 차이를 절대값으로 s 에 저장해준다.
        s.append(abs(c1s-c2s))
        m += 1


T = int(input())
for tc in range(1, T+1):
    # 식재료의 수 N
    N = int(input())
    # 시너지 정보
    S = [list(map(int, input().split())) for _ in range(N)]
    # 식재료를 담아둔 i
    i = deque(i for i in range(N))
    # 식재료의 시너지 정보의 차이를 담을 s
    s = deque()

    yes_chef()

    # 시너지의 차이 중 최소인 값을 출력
    print(f'#{tc} {min(s)}')