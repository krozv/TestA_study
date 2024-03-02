# 해당 문제에서 계산은 우선순위를 고려하지 않고 왼쪽에서 오른쪽으로 진행
def dfs(n,lst):
    if n == len(oper_card):
        oper_all.append(lst)
        return
    prev = 0
    for k in range(len(oper_card)):
        if visited[k] == 0 and prev != oper_card[k]:
            prev = oper_card[k]
            visited[k] = 1
            dfs(n+1,lst + [oper_card[k]])
            visited[k] = 0

def my_cal(operator, a, b):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    else:
        return int(a/b)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    oper_num  = list(map(int,input().split()))
    oper_card = []
    oper_card += ['+'] * oper_num[0]
    oper_card += ['-'] * oper_num[1]
    oper_card += ['*'] * oper_num[2]
    oper_card += ['/'] * oper_num[3]
    visited = [0] * len(oper_card)
    oper_all = []
    dfs(0,[])
    # 어차피 중복되는 것 없이 모든 경우의 수를 oper_all에 받았으므로, popleft 대신 pop 사용해도 같은 결과
    num_card = list(map(int,input().split()))
    max_result = -987654321
    min_result = 987654321
    det_continue = True
    for oper in oper_all:
        prev = num_card[0]
        for i in range(1,N):
            prev = my_cal(oper[-i], prev, num_card[i])
            if prev > 100000000 or prev < -100000000:
                det_continue = False
                break
        if det_continue == True:
            if max_result < prev:
                max_result = prev
            if min_result > prev:
                min_result = prev
        else:
            det_continue = True
            break
    if min_result >= max_result:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} {max_result - min_result}")
