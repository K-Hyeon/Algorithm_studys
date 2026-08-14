T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    t = input()
    matrix = [list(input().strip()) for _ in range(100)]
    max_val = 0
    #가로 세로 두번 검사
    for _ in range(2):
        #2차원 배열
        for row in matrix:
            #에서 행 검사
            #회문의 기본 길이 1 한글자도 회문이기 때문에

            for curr_index in range(100):
                palindrome_length = 1
                # 한행의 한열씩
                left = curr_index - 1
                right = curr_index + 1
                #우선 오른쪽과 본인을 비교해서 같으면 다를때까지 right += 1씩 함
                while right < 100 and row[curr_index] == row[right]:
                    right += 1
                    #회문길이를 늘림
                    palindrome_length += 1
                #지금 right는 본인과 다른 상태, 이 때 왼쪽과 비교함
                while left >= 0 and right < 100 and row[left] == row[right]:
                    #그래서 같으면 회문 길이를 늘림
                    palindrome_length += 2
                    #그리고 왼쪽, 오른쪽을 1씩 늘림
                    left -= 1
                    right += 1
                #모든 반복문이 끝나면 최댓값 갱신
                max_val = max(max_val, palindrome_length)

        matrix = list(map(list, zip(*matrix[::-1])))
    print(f'#{t} {max_val}')