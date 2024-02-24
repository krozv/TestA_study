# 4012_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY2i7WQ6i8EDFAXh&contestProbId=AWIeUtVakTMDFAVH&probBoxId=AY3KVArKm3gDFAXh&type=PROBLEM&problemBoxTitle=A%ED%98%95_240224&problemBoxCnt=4
'''
T = int(input())

for tc in range(T):
    n = int(input())
    subset = [] # 재료를 둘로 나누기 위한 길이가 n/2인 부분집합
    food = [list(map(int, input().split())) for _ in range(n)]
    idx = [i for i in range(n)] # 전체재료 - 음식1 재료를 구하기 위한 list
    result = 20000 # (min(음식1-음식2)을 계산하기 위해 충분히 큰 수

    # 길이가 n/2인 부분집합 - 음식1의 재료
    for i in range(1<<n):
        s = []
        for j in range(n):
            if i & (1<<j):
                s.append(j)
        if len(s) == n/2:
            subset.append(s)

    # 두 음식 값의 차이 계산
    for food1 in subset:
        food2 = list(set(idx).difference(food1)) # 음식2의 재료
        score1 = 0 # 음식 1의 값
        score2 = 0 # 음식 2의 값

        for i1 in range(int(n/2)): # food에서의 재료1의 inddex
            for i2 in range(i1+1, int(n/2)): # food에서의 재료2의 inddex
                # 음식1
                x1 = food1[i1]
                y1 = food1[i2]
                # 음식2
                x2 = food2[i1]
                y2 = food2[i2]

                # 음식값에 각 재료 값을 더함
                score1 += food[x1][y1] + food[y1][x1]
                score2 += food[x2][y2] + food[y2][x2]

        # 값의 차이가 최소가 되는 값을 저장
        if abs(score1 - score2) < result:
            result = abs(score1-score2)

    print(f'#{tc+1} {result}')