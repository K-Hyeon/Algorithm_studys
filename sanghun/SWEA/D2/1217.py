

import sys
input = sys.stdin.readline


# N과 M을 입력받는데, N을 M번 곱해준 값을 재귀로 구현해야한다 
# 재귀는 스스로 다시 호출해야 재귀이다 

def multiplication(a, b):
    # 입력값과 기준값을 정해준다 
    # Base Case: 어떤 수의 0제곱은 1
    if b == 0:
        return 1

    # 재귀 스텝인데, 처음 a의 값에 b가 하나씩 줄어가면서 위에 스탑 조건만 넣어준다
    return a * multiplication(a, b-1)
    

for _ in range(10):
    number = int(input())
    N, M = map(int, input().split())

    result = multiplication(N, M)


    print(f"#{number} {result}")
