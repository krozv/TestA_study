# 4008. 숫자 만들기
### 코드
411ms
```python
def dfs(i, plus, sub, mul, div, cal):
    global min_cal, max_cal
    if i == N:
        if min_cal > cal:
            min_cal = cal
        if max_cal < cal:
            max_cal = cal
        return
    if plus > 0:
        dfs(i+1,plus-1, sub, mul, div, cal+nums[i])
    if sub > 0:
        dfs(i+1, plus, sub-1, mul, div, cal-nums[i])
    if mul > 0:
        dfs(i+1, plus, sub, mul-1, div, cal*nums[i])
    if div > 0:
        if cal >= 0:
            dfs(i+1, plus, sub, mul, div-1, cal//nums[i]) #소수점 아래 버린다고 나와있음
        else:
            dfs(i+1, plus, sub, mul, div-1, -((-cal)//nums[i]))
T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    O = list(map(int, input().split())) # 연산자
    nums = list(map(int, input().split()))
    min_cal = 100000000 #최소 계산 결과
    max_cal = -100000000#최대 계산 결과
    dfs(1, O[0], O[1], O[2], O[3], nums[0])
    print(f'#{tc} {max_cal - min_cal}')
```
**틀렸던 부분...**

나누기를 할 때 소수점을 버리라고 나와있었음..
-3//2 는 `-2`가 나옴. 원래 `-3/2 = -1.5`이므로 결과 값이 `-1`이 나와야 함. 따라서 
```python
if cal >= 0:
    dfs(i+1, plus, sub, mul, div-1, cal//nums[i]) #소수점 아래 버린다고 나와있음
else:
    dfs(i+1, plus, sub, mul, div-1, -((-cal)//nums[i]))
```
맞춤으로 코드 변경