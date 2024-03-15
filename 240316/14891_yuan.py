from collections import deque

def go_clock(lst):
    lst = deque(lst)
    t = lst.pop()
    lst.appendleft(t)
    lst = list(lst)
    return lst
def back_clock(lst):
    lst = deque(lst)
    t = lst.popleft()
    lst.append(t)
    lst = list(lst)
    return lst

def f(check, wheel):

    for num in range(4):
        if check[num-1] == 1:
            wheel[num - 1] = go_clock(wheel[num - 1])
        elif check[num-1] == -1:
            wheel[num - 1] = back_clock(wheel[num - 1])
        else:
            continue
    return wheel

wheel = []
for _ in range(4):
    wheel.append(list(map(int,list(input()))))
for i in range(4):
    for j in range(8):
        wheel[i][j] = int(wheel[i][j])

# print(wheel)
k = int(input()) # 회전수
lst = []
for _ in range(k):
    lst.append(list(input().split()))

for i in lst:
    check = [0,0,0,0]
    visit = [0,0,0,0]
    num,d = int(i[0]), int(i[1])
    check[num-1] = d
    visit[num-1] = 1
    if num>1:
        while num >1:
            visit[num-2] = 1
            if wheel[num-1][6] != wheel[num-2][2]:
                check[num-2] = - check[num-1]
                num-=1
            else:
                break
    if num<=3:
        while num<=3:
            if visit[num]:
                num+=1
            else:
                visit[num] = 1
                if wheel[num-1][2] != wheel[num][6]:
                    check[num]= - check[num-1]
                    num+=1
                else:
                    break

    new_wheel = f(check, wheel)
    wheel = new_wheel

total = 0
for x in range(4):
    if wheel[x][0]:
        total += 2**x
print(total)