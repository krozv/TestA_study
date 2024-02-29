# 1486_swea(장훈이의 높은 선반)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY2i7WQ6i8EDFAXh&contestProbId=AV2b7Yf6ABcBBASw&probBoxId=AY3s4YIKB4kDFAUZ&type=PROBLEM&problemBoxTitle=A%ED%98%95_240302&problemBoxCnt=6
'''
def bfs(i, h):
    global result
    if h >= b and h <= result:
        result = h
        return

    if i == n:
        return

    bfs(i + 1, h+people[i])
    bfs(i + 1, h)

T = int(input())

for tc in range(T):
    n, b = map(int, input().split())
    people = list(map(int, input().split()))
    result = sum(people)

    bfs(0,0)

    print(f'#{tc+1} {result-b}')