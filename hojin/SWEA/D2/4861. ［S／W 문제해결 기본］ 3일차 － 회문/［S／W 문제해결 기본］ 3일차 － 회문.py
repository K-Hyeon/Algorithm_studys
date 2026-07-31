T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # n x n의 글자판이 주어지고 m은 회문의 길이이다.
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    result = ""
   #가로 회문 찾기 0,0 0,1 0,2
    for i in range(n):
        is_palindrome = True
        for j in range(n-m+1):
            word = matrix[i][j:j+m]
            if word == word[::-1]:
                result = word
                break
        if result:
            break

    # 세로회문 0,0 1,0 2,0
    if result == "":
        for i in range(n):
            is_palindrome = True
            for j in range(n - m +1):
                word = "".join([matrix[k][i] for k in range(j,j+m)])

                if word == word[::-1]:
                    result = word

    print(f"#{test_case} {result}")