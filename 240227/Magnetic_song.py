# 1220_swea
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY2i7WQ6i8EDFAXh&contestProbId=AV14hwZqABsCFAYD&probBoxId=AY3WBtm6TUcDFAUZ&type=PROBLEM&problemBoxTitle=A%ED%98%95_240227&problemBoxCnt=4
'''
def clear(start):
    x, y = start
    color = arr[y][x]
    if color == 1:
        line = [i[x] for i in arr[y:]]
        d_color = 2
    else:
        line = [i[x] for i in arr[:y]]
        d_color = 1
 
    if d_color not in line:
        arr[y][x] = 0
 
def deadrock(arr):
    global cnt
    color = 0
 
    for i in range(100):
        if arr[i] not in [0,color]:
            cnt += 1
            color = arr[i]
 
for tc in range(10):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
 
    for y in range(100):
        for x in range(100):
            if arr[y][x] in (1, 2):
                clear((x,y))
 
    for x in range(100):
        tmp = [i[x] for i in arr]
        deadrock(tmp)
 
    print(f'#{tc+1} {int(cnt/2)}')