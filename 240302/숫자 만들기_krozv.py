# 14888. 연산자 끼워넣기
def f(n, arr):
    global max_val
    global min_val
    if len(path) == n:
        # print(path)
        # print(calculator(path))
        val = calculator(path)
        max_val = max(max_val, val)
        min_val = min(min_val, val)
        return
    if arr[0] > 0:
        path.append(oper_list[0])
        arr[0] -= 1
        f(n, arr)
        arr[0] += 1
        path.pop()
    if arr[1] > 0:
        path.append(oper_list[1])
        arr[1] -= 1
        f(n, arr)
        arr[1] += 1
        path.pop()
    if arr[2] > 0:
        path.append(oper_list[2])
        arr[2] -= 1
        f(n, arr)
        arr[2] += 1
        path.pop()
    if arr[3] > 0:
        path.append(oper_list[3])
        arr[3] -= 1
        f(n, arr)
        arr[3] += 1
        path.pop()

def calculator(op):
    stk = [num_list[0]]
    for i in range(len(op)):
        if op[i] == '+':
            stk[0] = stk[0] + num_list[i+1]
        elif op[i] == '-':
            stk[0] -= num_list[i+1]
        elif op[i] == '*':
            stk[0] *= num_list[i+1]
        elif op[i] == '/':
            if stk[0] < 0:
                stk[0] = -(-stk[0] // num_list[i+1])
            else:
                stk[0] //= num_list[i+1]
    return stk[0]


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    operator = list(map(int, input().split()))  # +, -, *, // 개수
    num_list = list(map(int, input().split()))
    oper_list = ['+', '-', '*', '/']
    # a, b, c, d = operator
    path = []
    max_val = -1e9
    min_val = 1e9
    f(len(num_list)-1, operator)



    # for operator in op_lst:
    #     val = calculator(operator, num_list)
    #     max_val = max(max_val, val)
    #     min_val = min(min_val, val)
    #
    print(f'#{t} {max_val-min_val}')