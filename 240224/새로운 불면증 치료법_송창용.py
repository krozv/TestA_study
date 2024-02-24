# 1288_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY2i7WQ6i8EDFAXh&contestProbId=AV18_yw6I9MCFAZN&probBoxId=AY3KVArKm3gDFAXh&type=PROBLEM&problemBoxTitle=A%ED%98%95_240224&problemBoxCnt=4
'''
T = int(input())
verify = [0,1,2,3,4,5,6,7,8,9] # 검증 수

for tc in range(T):
    sheep = [] # 새로운 숫자를 저장하기 위한 list
    n = int(input())
    cnt = 0 # 몇 번째인지 확인

    while sheep != verify: # sheep이 verify와 같아질 떄까지
        cnt += 1
        num = n * cnt # 양 * 횟수
        for s in str(num):
            if int(s) not in sheep: # sheep에 값이 없으면 저장
                sheep.append(int(s))
        sheep.sort() # 정렬

    print(f'#{tc+1} {num}')