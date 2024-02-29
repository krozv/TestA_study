# 5658_swea(보물상자 비밀번호)
'''
https://swexpertacademy.com/main/talk/solvingClub/problemView.do?solveclubId=AY2i7WQ6i8EDFAXh&contestProbId=AWXRUN9KfZ8DFAUo&probBoxId=AY3s4YIKB4kDFAUZ&type=PROBLEM&problemBoxTitle=A%ED%98%95_240302&problemBoxCnt=6
'''
def rotate(i):
    global result

    for i in range(0, n-share-1, share): # 한 변의 길이만큼 slicing
        num = int(''.join(number[i:i+share]), 16) # 각 값을 10진수로 변경
        if num not in result: # 값이 없다면 추가
            result.append(num)

    number.insert(0,number.pop()) # 회전

T = int(input())

for tc in range(T):
    n, k = map(int, input().split())
    number = list(input())
    result = [] # 값 저장
    share = n//4 # 한변의 길이

    for i in range(n): # n번만큼 반복
        rotate(i)

    result.sort(reverse=True) # 정렬

    print(f'#{tc+1} {result[k-1]}')