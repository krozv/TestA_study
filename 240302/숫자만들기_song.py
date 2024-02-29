# 4008_swea(숫자만들기)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY2i7WQ6i8EDFAXh&contestProbId=AWIeRZV6kBUDFAVH&probBoxId=AY3s4YIKB4kDFAUZ&type=PROBLEM&problemBoxTitle=A%ED%98%95_240302&problemBoxCnt=6
'''
def dfs(i, n, s, a,b,c,d): # i : 현재 수, n : 골라야 할 수
    if i == n:
        if a == 0 and b == 0 and c == 0 and d == 0:
            idx.append(s)
        return
    dfs(i + 1, n, s+'+', a - 1, b, c, d)
    dfs(i + 1, n, s+'-', a, b - 1, c, d)
    dfs(i + 1, n, s+'*', a, b, c - 1, d)
    dfs(i + 1, n, s+'/', a, b, c, d - 1)
 
T = int(input())
 
for tc in range(T):
    n = int(input())
    a, b, c, d = map(int, input().split())
    number = list(map(int, input().split()))
    idx, valid = [], [[] for _ in range(n)]
    min_result = 9**12
    max_result = -9**12
 
    dfs(0, n-1, '', a, b, c, d)
 
    for i in idx:
        num = number[0]
        for j in range(len(i)):
            if i[j] == '+':
                num += number[j + 1]
            elif i[j] == '-':
                num -= number[j + 1]
            elif i[j] == '*':
                num *= number[j + 1]
            else:
                num = int(num / number[j + 1])
 
        if num >= max_result:
            max_result = num
        if num <= min_result:
            min_result = num
 
    print(f'#{tc+1} {max_result - min_result}')