def turn(n, d):
    if d == 1:
        print(gear[n])
        gear[n] = gear[n].insert(0, gear[n].pop())
        print(gear[n])
    elif d == -1:
        print(gear[n])
        gear[n] = gear[n].insert(-1, gear[n].pop(0))
        print(gear[n])

def check(n, d):
    direction[n] = d
    if n == 0 or n == 3 or d == 0:
        return
    if gear[n][6] != gear[n-1][2]:
        d *= -1
        check(n-1, d)
    else:
        check(n-1, 0)
    if gear[n][2] != gear[n+1][6]:
        d *= 1
        check(n+1, d)
    else:
        check(n+1, 0)
    return


gear = [list(input()) for _ in range(4)]
k = int(input())
rotate = [list(map(int, input().split())) for _ in range(k)]
# 2, 6
print(gear)
for c in range(k):
    direction = [0] * 4
    check(rotate[c][0], rotate[c][-1])

    for i, d in enumerate(direction):
        if d == 1:
            tmp = gear[i]
            tmp = tmp.insert(0, tmp[i].pop())
            gear[i] = tmp
        elif d == -1:
            tmp = gear[i]
            tmp = tmp[i].insert(-1, tmp[i].pop(0))
            gear[i] = tmp

print(gear)