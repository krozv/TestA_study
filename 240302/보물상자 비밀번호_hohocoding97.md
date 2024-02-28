# 5658. 보물상자 비밀번호
### 코드
144ms. 큐 사용해서 풀었음
```python
#큐써야할 것 같은 느낌
T = int(input())
for tc in range(1, 1+T):
    N, K = map(int,input().split()) # N: 숫자 개수
    data = list(input()) 
    nums = set()
    for _ in range(N//4):   #N//4번 반복
        for i in range(4):  #숫자 4등분을 위해
            nums.add(int(''.join(data[(N//4)*i:(N//4)*(i+1)]), 16)) #4등분해서 16진수 문자열을 int형으로
        data.append(data.pop(0)) #앞에서 빼서 뒤로 넣기
    all_key = sorted(nums,reverse=True) # nums에 넣은 숫자들을 오름차순으로 정렬
    print(f'#{tc} {all_key[K-1]}')      #K번째 숫자 출력(따라서 K-1번 인덱스 출력)
```
참고로 데크 사용해서 할려고 했는데 데크에서 join이 안써져서 포기함

**16진수 문자열을 int형으로 바꾸기**
`int(str_16, 16)`