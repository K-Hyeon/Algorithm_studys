"""
N은 10 이상 100 이하
M은 5 이상 N 이하

최소 조건 : N, M  = (10, 5)
최대 조건 : N, M  = (100, 100)


회문은 세로로도 존재할 수 있음
회문은 하나만 존재

내 목표
1. 우선 가로로 존재하는 회문 찾기(N줄 * (N - M + 1))
2. 배열 90도 회전 시킨 다음 1번 반복 

위 동작에서 최대 연산 : N, M (100, 5), 회문이 오른쪽 위에서 부터 세로로 존재하는 경우
-> 2(100 * 96) + 2*100 약 2만번의 연산 충분할 듯
"""

def findPalindrome(arr, N, M):
    for row in arr:
        for start_i in range(N- M +1):
            if row[start_i : start_i + M] ==  row[start_i : start_i + M][::-1]:
                return row[start_i : start_i + M]
    return False

testCase = int(input())


for testCaseNum in range(testCase):
    N, M = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    answer = findPalindrome(arr, N, M)
    if answer:
        print(f"#{testCaseNum + 1} {''.join(answer)}")
    else:
        rotated_arr = list(map(list,zip(*arr[::-1])))
        rotated_answer = findPalindrome(rotated_arr, N, M)
        print(f"#{testCaseNum + 1} {''.join(rotated_answer)}")
        