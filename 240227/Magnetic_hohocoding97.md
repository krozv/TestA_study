# 1220. Magnetic
### 코드
239ms

stack사용해서 풀기
```python
#무언가 열 단위로 스택을 잘 쓰면 될 것 같은 느낌스
for tc in range(1,11):
    input()
    data = [list(map(int, input().split())) for _ in range(100)] #100*100크기의 배열
    result = 0
    for j in range(100): #열 순회
        stack = []
        for i in range(100): #행 순회
            if data[i][j] == 1: #N극인 경우 무조건 스택에 넣어
                stack.append(1)
            if data[i][j] == 2: #s극인 경우 스택에 가장 최근에 넣은게 N극이라면 result += 1
                if stack and stack[-1] == 1:
                    stack.append(2)
                    result += 1
    print(f'#{tc} {result}')
```